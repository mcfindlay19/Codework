"""
Project Name: GIS Geoprocessing Script
Description: This script processes GIS vector datasets to ensure they are using 
             the NAD83 UTM Zone 12N coordinate system. It checks projections, 
             defines undefined ones, and reprojects incorrect datasets.
Author: Matt Findlay, mfindlay@ucalgary.ca
Version: 1.0 - Created base work flow
         1.1 - Tidied up code, making functions
         1.2 - fixed bug where i forgot to change name of reprojected items
         1.3 - Tidied up output
         1.4 - Added comments
         1.5 - Added logic for overwritting files instead of creating new ones
Date: Jan 31, 2025
Usage: Run the script and provide the workspace directory containing GIS datasets.
       It will process all shapefiles and feature classes in the workspace.
"""
import arcpy
import os

def get_datasets(workspace):
    """Gets all shapefiles and feature classes in the workspace."""
    arcpy.env.workspace = workspace
    return arcpy.ListFeatureClasses() or []

def check_projection(dataset):
    """Checks if dataset has a spatial reference and returns it."""
    desc = arcpy.Describe(dataset)
    return desc.spatialReference if desc.spatialReference else None, desc.shapeType

def define_projection(dataset):
    """Assigns NAD 1983 projection (EPSG: 4269) if none exists."""
    arcpy.DefineProjection_management(dataset, arcpy.SpatialReference(4269))

def project_dataset(dataset, workspace):
    """Projects dataset to NAD83 UTM Zone 12N (EPSG: 26912) while keeping the same name."""
    dataset_name, ext = os.path.splitext(os.path.basename(dataset))
    output_path = os.path.join(workspace, dataset_name + "_temp" + ext)  # Create a temporary output file
    
    # Run the projection tool
    arcpy.Project_management(dataset, output_path, arcpy.SpatialReference(26912))
    
    # Remove the original file and rename the new one to keep the same name
    arcpy.Delete_management(dataset)
    arcpy.Rename_management(output_path, dataset)

def main():
    """Main function to process GIS data."""
    # Prompt user for the workspace directory
    workspace = input("Enter workspace path: ")
    
    # Retrieve all vector datasets (shapefiles or feature classes)
    datasets = get_datasets(workspace)
    
    # Initialize counters for datasets
    total = len(datasets)
    correct_proj = 0
    changed_proj = 0
    undefined_proj = 0
    shape_counts = {"Point": 0, "Polyline": 0, "Polygon": 0}
    undefined_names = []
    
    # Process each dataset
    for dataset in datasets:
        spatial_ref, shape_type = check_projection(dataset)
        
        # Count shape types
        if shape_type in shape_counts:
            shape_counts[shape_type] += 1
        
        # If no projection is found, assign GCS NAD83 (EPSG: 4269)
        if not spatial_ref or spatial_ref.name == "Unknown":
            undefined_proj += 1
            undefined_names.append(dataset)
            define_projection(dataset)
            spatial_ref = arcpy.SpatialReference(4269)  # Set to known state for further checks
        
        # If dataset is not in NAD83 UTM Zone 12N, reproject it
        if spatial_ref.factoryCode != 26912:
            changed_proj += 1
            project_dataset(dataset, workspace)
        else:
            correct_proj += 1
    
    # Print summary of processing results
    print(f"Total vector datasets processed: {total}")
    print("Shapefile breakdown by geometry type:")
    for shape, count in shape_counts.items():
        print(f"  {shape}: {count}")
    print(f"Datasets already in NAD83 UTM 12N: {correct_proj}")
    print(f"Datasets reprojected to NAD83 UTM 12N: {changed_proj}")
    print(f"Datasets that had undefined projections fixed: {undefined_proj}")
    if undefined_names:
        print("Datasets without a defined spatial reference:")
        for name in undefined_names:
            print(f"  {name}")

# Entry point for script execution
if __name__ == "__main__":
    main()
