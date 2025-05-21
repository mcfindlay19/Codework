# Batch Verify Projections
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/platform-ArcGIS--Pro%20%7C%20arcpy-orange)

This ArcGIS Pro Python script tool batch-processes GIS vector datasets to ensure they have valid spatial references. It defines missing projections and reprojects all datasets to a specified coordinate system (default is NAD83 UTM Zone 12N). The tool provides progress updates and handles common errors gracefully.

## Overview

- **Author:** Matt Findlay  
- **Date:** February 3, 2025  
- **Latest Version:** 1.5  
- **Script Tool Name:** `BatchVerifyProjections`   

## Features

- Validates projections for all vector datasets in a workspace.
- Defines undefined projections using user-specified spatial reference.
- Reprojects datasets to NAD83 UTM Zone 12N.
- Tracks shape types and provides processing summaries.
- Integrates a step progressor for execution feedback.
- Includes robust error handling per dataset and globally.

## Installation

This script is intended to be run from a custom script tool in ArcGIS Pro.

### 1. Requirements

- ArcGIS Pro with Python and `arcpy`
- Vector data in a geodatabase or shapefile format

### 2. Clone the repository
```bash
   git@github.com:mcfindlay19/Codework.git
   cd week9
```

### 3. Setup

1. Create a custom toolbox (`*.atbx`) in ArcGIS Pro (e.g., `BatchVerifyProjections.atbx`).
2. Right-click the toolbox → **Add > Script**, and configure it:
   - **Name:** `BatchVerifyProjections`
   - **Label:** `Batch Verify Projections`
   - **Script File:** Point to this script (`BatchVerifyProjections.py`)
   - **Use relative paths:**  Enabled

### 4. Configure Parameters

In the Script Tool's **Properties**, define two parameters:

| # | Label                               | Data Type                | Direction |
|---|-------------------------------------|---------------------------|-----------|
| 1 | Input Workspace or Feature Dataset | Workspace or Feature Dataset | Input     |
| 2 | Spatial Reference System            | Spatial Reference         | Input     |

### 5. Run the Tool

1. Open the script tool in ArcGIS Pro.
2. Select a folder or feature dataset containing shapefiles or feature classes.
3. Choose a spatial reference to apply to undefined datasets.
4. Click **Run**.

### 6. Output

- Reprojected datasets are renamed and replace the originals.
- Summary messages include:
  - Total datasets processed
  - Geometry type counts
  - Count of datasets reprojected, unchanged, or assigned a spatial reference

## File Structure

```
BatchVerifyProjections/
├── BatchVerifyProjections.py    # Main script
├── instructions.md              # Assignment and setup instructions
└── README.md                    # You're here
```


## Error Handling

- Warnings for missing datasets or unknown spatial references.
- Errors are logged per dataset and summarized.
- Global error catch ensures graceful script termination.

## Version History

- **1.0** – Initial working version
- **1.1** – Converted input to `arcpy.GetParameterAsText`
- **1.2** – Integrated step progressor
- **1.3** – Dataset-level error handling
- **1.4** – Handled case with no vector datasets
- **1.5** – Global script error handling

## License

This project is licensed under the MIT License.
