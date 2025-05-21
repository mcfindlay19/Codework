"""
Project Name: Wildlife Survey Data Import & Analysis
Description: 
    This script imports wildlife survey data from a CSV file, converts coordinate formats, 
    and creates a point feature class in ArcGIS Pro. It also analyzes the dataset to determine 
    the presence of species at different locations and identifies extreme geographical points.

Author: Matt Findlay, mfindlay@ucalgary.ca
Version History:
    v1.0 - Initial script implementation
    v1.1 - Fixed missing point geometry issue
    v1.2 - Corrected east-west mirroring of coordinates
    v1.3 - Improved error handling and validation
    v1.4 - Final testing and optimization

Date: Feb 3, 2025
Usage:
    - Run this script as a geoprocessing tool in ArcGIS Pro.
    - Provide the CSV input file and specify the output feature class location.
    - The script will create a feature class with points representing survey locations.
    - Outputs analysis results, including the number of observations and extreme locations.
"""

import arcpy
import os
import csv

def dms_to_dd(dms_str):
    """Converts DMS format (e.g., 47D-27M-56.38) to Decimal Degrees."""
    try:
        parts = dms_str.split('D-')
        degrees = float(parts[0])
        minutes_seconds = parts[1].split('M-')
        minutes = float(minutes_seconds[0])
        seconds = float(minutes_seconds[1].replace('S', ''))
        
        dd = degrees + (minutes / 60) + (seconds / 3600)
        return dd  # Ensure correct conversion
    except Exception as e:
        arcpy.AddError(f"Error converting DMS to DD: {e}")
        return None

def import_csv_to_feature_class(csv_path, output_fc):
    """Imports a CSV file into a feature class, converting coordinates."""
    try:
        arcpy.env.overwriteOutput = True
        spatial_ref = arcpy.SpatialReference(4326)  # WGS 1984
        
        # Create feature class
        arcpy.CreateFeatureclass_management(os.path.dirname(output_fc),
                                            os.path.basename(output_fc),
                                            "POINT",
                                            spatial_reference=spatial_ref)
        
        # Add fields
        fields = ["Year", "SurveyID", "Presence", "sLatitude", "sLongitude", "Latitude", "Longitude"]
        field_types = ["LONG", "LONG", "SHORT", "TEXT", "TEXT", "DOUBLE", "DOUBLE"]
        for field, f_type in zip(fields, field_types):
            arcpy.AddField_management(output_fc, field, f_type)
        
        # Read CSV and insert points
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Using InsertCursor to add geometry
            with arcpy.da.InsertCursor(output_fc, ["SHAPE@XY"] + fields) as cursor:
                for row in reader:
                    try:
                        lat_dd = dms_to_dd(row['sLatitude'])
                        lon_dd = -dms_to_dd(row['sLongitude'])  # Mirror east-west
                        
                        if lat_dd is None or lon_dd is None:
                            continue  # Skip invalid rows
                        
                        # Create geometry
                        point_geometry = (lon_dd, lat_dd)  # (X, Y) = (Longitude, Latitude)
                        
                        cursor.insertRow([
                            point_geometry,  # Insert geometry first
                            int(row['Year']),
                            int(row['SurveyID']),
                            int(row['Presence']),
                            row['sLatitude'],
                            row['sLongitude'],
                            lat_dd,
                            lon_dd
                        ])
                    except Exception as e:
                        arcpy.AddWarning(f"Skipping row due to error: {e}")
    except Exception as e:
        arcpy.AddError(f"Error importing CSV: {e}")


def analyze_feature_class(fc):
    """Analyzes the feature class for species presence statistics."""
    try:
        query = "Presence = 1"
        fields = ["SurveyID", "Latitude", "Longitude"]
        presence_count = 0
        locations = []
        
        with arcpy.da.SearchCursor(fc, fields, query) as cursor:
            for row in cursor:
                presence_count += 1
                locations.append((row[0], row[1], row[2]))
        
        # Sort to find extreme locations
        northmost = sorted(locations, key=lambda x: x[1], reverse=True)[:3]
        southmost = sorted(locations, key=lambda x: x[1])[:3]
        eastmost = sorted(locations, key=lambda x: x[2], reverse=True)[:3]
        westmost = sorted(locations, key=lambda x: x[2])[:3]
        
        # Output results
        arcpy.AddMessage(f"Total locations with species present: {presence_count}")
        for title, group in zip(["Northmost", "Southmost", "Eastmost", "Westmost"],
                                [northmost, southmost, eastmost, westmost]):
            arcpy.AddMessage(f"{title} observations:")
            for obs in group:
                arcpy.AddMessage(f"  SurveyID {obs[0]} at ({obs[1]}, {obs[2]})")
    except Exception as e:
        arcpy.AddError(f"Error analyzing feature class: {e}")

def main():
    """Main function to execute script tool."""
    try:
        csv_path = arcpy.GetParameterAsText(0)
        output_fc = arcpy.GetParameterAsText(1)
        
        if not csv_path or not output_fc:
            arcpy.AddError("Input CSV or output feature class not provided.")
            return
        
        arcpy.AddMessage("Importing CSV to feature class...")
        import_csv_to_feature_class(csv_path, output_fc)
        
        arcpy.AddMessage("Analyzing feature class...")
        analyze_feature_class(output_fc)
        
        arcpy.AddMessage("Script completed successfully.")
    except Exception as e:
        arcpy.AddError(f"Script failed: {e}")

if __name__ == "__main__":
    main()
