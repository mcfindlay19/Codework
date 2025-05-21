"""
Project: Topographic Roughness Index (TRI) Computation Tool
Description: This script calculates the Topographic Roughness Index (TRI) for a given
             DEM (Digital Elevation Model) and saves the output in an 'output' directory
             within the same folder as the input DEM
Author: Matt Findlay, mfindlayucalgary.ca
Version: 1.0 - Initial version implementing TRI calculation using focal statistics and map algebra.

Date: Feb 4, 2025
Usage:
  - Ensure the input DEM is in a valid raster format.
  - Run this script in ArcGIS Pro using the Python environment with Spatial Analyst enabled.
  - The output TRI raster will be stored in an 'output' directory within the input DEM location.
Dependencies:
  - ArcPy with Spatial Analyst extension enabled
  - Input DEM in raster format
Formula for TRI:
  TRI = SquareRoot(2 + F2 + 9*D2 - 2*D1*F1)
  where:
  - D2: Squared elevation raster (DEM * DEM)
  - F1: Sum of elevation pixels in a 3x3 window
  - F2: Sum of squared elevation pixels in a 3x3 window
Output:
  - A raster file named '<input_name>_tri.tif' stored in the 'output' directory.
"""

import arcpy
from arcpy.sa import *
import os

# Enable the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Define the function to compute TRI
def compute_tri(input_dem):
    try:
        # Set the workspace to the input DEM location
        workspace = os.path.join(os.path.dirname(input_dem), "output")
        if not os.path.exists(workspace):
            os.makedirs(workspace)
        arcpy.env.workspace = workspace
        arcpy.env.overwriteOutput = True
        
        # Extract input filename without extension
        input_name = os.path.splitext(os.path.basename(input_dem))[0]
        output_name = f"{input_name}_tri.tif"
        
        # Create a raster layer of squared elevation values (D2)
        D2 = Raster(input_dem) * Raster(input_dem)
        D2_tif = os.path.join(workspace, "D2.tif")
        D2.save(D2_tif)
        
        # Compute sum of elevation pixels in a 3x3 window (F1) using NODATA option
        F1 = FocalStatistics(input_dem, NbrRectangle(3, 3, "CELL"), "SUM", "NODATA")
        F1_tif = os.path.join(workspace, "F1.tif")
        F1.save(F1_tif)
        
        # Compute sum of squared elevation pixels in a 3x3 window (F2) using NODATA option
        F2 = FocalStatistics(D2, NbrRectangle(3, 3, "CELL"), "SUM", "NODATA")
        F2_tif = os.path.join(workspace, "F2.tif")
        F2.save(F2_tif)
        
        # Compute TRI using the formula: TRI = SquareRoot(2 + F2 + 9*D2 - 2*D1*F1)
        D1 = Raster(input_dem)
        TRI = SquareRoot(2 + F2 + 9 * D2 - 2 * D1 * F1)
        TRI_tif = os.path.join(workspace, output_name)
        TRI.save(TRI_tif)
        
        # Clean up intermediate files
        arcpy.Delete_management(D2_tif)
        arcpy.Delete_management(F1_tif)
        arcpy.Delete_management(F2_tif)
        
        print("TRI computation completed successfully. Output saved at:", TRI_tif)
    except Exception as e:
        print("Error encountered:", e)
    finally:
        arcpy.CheckInExtension("Spatial")

# Main execution for standalone script
if __name__ == "__main__":
    # User input
    input_dem = arcpy.GetParameterAsText(0)  # Input DEM
    
    # Run the TRI computation function
    compute_tri(input_dem)
