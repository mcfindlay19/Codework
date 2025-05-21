"""
Project Name: Batch Verify Projections
Description: This script processes GIS vector datasets by checking projections,
             defining undefined projections, and reprojecting datasets into
             any projection
Author: Matt Findlay, mfindlayucalgary.ca
Version: 1.0 - Copy files over
         1.1 - Change input method to work with ArcGIS Pro Scripts
         1.2 - Added step progressor
         1.3 - Added error handling for each dataset
         1.4 - Added error handling for if no vector datasets present
         1.5 - Added error handling for script-wide error
Date: Feb 3, 2025
Usage: This script is designed to be used as an ArcGIS script tool.
       It requires the user to input a workspace containing vector datasets
       and specify a spatial reference for undefined datasets.
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

def define_projection(dataset, spatial_ref):
    """Assigns user-specified spatial reference if none exists."""
    arcpy.DefineProjection_management(dataset, spatial_ref)

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
    try:
        # Set script tool parameters
        workspace = arcpy.GetParameterAsText(0)  # Expected data type: Workspace or Feature Dataset
        spatial_ref = arcpy.GetParameter(1)  # Expected data type: Spatial Reference
        
        # Retrieve all vector datasets (shapefiles or feature classes)
        datasets = get_datasets(workspace)
        total = len(datasets)
        
        if total == 0:
            arcpy.AddWarning("No vector datasets found in the specified workspace.")
            return
        
        # Initialize step progressor
        arcpy.SetProgressor("step", "Processing datasets...", 0, total, 1)
        
        # Initialize counters for datasets
        correct_proj = 0
        changed_proj = 0
        undefined_proj = 0
        shape_counts = {"Point": 0, "Polyline": 0, "Polygon": 0}
        undefined_names = []
        
        # Process each dataset
        for i, dataset in enumerate(datasets):
            try:
                spatial_ref_existing, shape_type = check_projection(dataset)
                
                # Count shape types
                if shape_type in shape_counts:
                    shape_counts[shape_type] += 1
                
                # If no projection is found, assign user-specified projection
                if not spatial_ref_existing or spatial_ref_existing.name == "Unknown":
                    undefined_proj += 1
                    undefined_names.append(dataset)
                    define_projection(dataset, spatial_ref)
                    spatial_ref_existing = spatial_ref  # Set to known state for further checks
                
                # If dataset is not in NAD83 UTM Zone 12N, reproject it
                if spatial_ref_existing.factoryCode != 26912:
                    changed_proj += 1
                    project_dataset(dataset, workspace)
                else:
                    correct_proj += 1
                
                # Update step progressor
                arcpy.SetProgressorPosition(i + 1)
            except Exception as dataset_error:
                arcpy.AddError(f"Error processing dataset {dataset}: {str(dataset_error)}")
        
        # Reset progressor
        arcpy.ResetProgressor()
        
        # Print summary of processing results
        arcpy.AddMessage(f"Total vector datasets processed: {total}")
        arcpy.AddMessage("Shapefile breakdown by geometry type:")
        for shape, count in shape_counts.items():
            arcpy.AddMessage(f"  {shape}: {count}")
        arcpy.AddMessage(f"Datasets already in NAD83 UTM 12N: {correct_proj}")
        arcpy.AddMessage(f"Datasets reprojected to NAD83 UTM 12N: {changed_proj}")
        arcpy.AddMessage(f"Datasets that had undefined projections fixed: {undefined_proj}")
        if undefined_names:
            arcpy.AddMessage("Datasets without a defined spatial reference:")
            for name in undefined_names:
                arcpy.AddMessage(f"  {name}")
    except Exception as main_error:
        arcpy.AddError(f"Unexpected error occurred: {str(main_error)}")
    finally:
        arcpy.ResetProgressor()

# Entry point for script execution
if __name__ == "__main__":
    main()
