# Batch Verify Projections

This ArcGIS Pro Python script tool batch-processes GIS vector datasets to ensure they have valid spatial references. It defines missing projections and reprojects all datasets to a specified coordinate system (default is NAD83 UTM Zone 12N). The tool provides progress updates and handles common errors gracefully.

## 🔍 Overview

- **Author:** Matt Findlay  
- **Date:** February 3, 2025  
- **Latest Version:** 1.5  
- **Script Tool Name:** `BatchVerifyProjections`  
- **Toolbox:** Custom Toolbox (`<Lastname>_Lab9.atbx`)  

## 🧭 Features

- Validates projections for all vector datasets in a workspace.
- Defines undefined projections using user-specified spatial reference.
- Reprojects datasets to NAD83 UTM Zone 12N.
- Tracks shape types and provides processing summaries.
- Integrates a step progressor for execution feedback.
- Includes robust error handling per dataset and globally.

## 🛠️ How to Use

This script is intended to be run from a custom script tool in ArcGIS Pro.

### 1. Setup

1. Create a custom toolbox (`*.atbx`) in ArcGIS Pro (e.g., `Findlay_Lab9.atbx`).
2. Right-click the toolbox → **Add > Script**, and configure it:
   - **Name:** `BatchVerifyProjections`
   - **Label:** `Batch Verify Projections`
   - **Script File:** Point to this script (`BatchVerifyProjections.py`)
   - **Use relative paths:** ✅ Enabled

### 2. Configure Parameters

In the Script Tool's **Properties**, define two parameters:

| # | Label                               | Data Type                | Direction |
|---|-------------------------------------|---------------------------|-----------|
| 1 | Input Workspace or Feature Dataset | Workspace or Feature Dataset | Input     |
| 2 | Spatial Reference System            | Spatial Reference         | Input     |

### 3. Run the Tool

1. Open the script tool in ArcGIS Pro.
2. Select a folder or feature dataset containing shapefiles or feature classes.
3. Choose a spatial reference to apply to undefined datasets.
4. Click **Run**.

### 4. Output

- Reprojected datasets are renamed and replace the originals.
- Summary messages include:
  - Total datasets processed
  - Geometry type counts
  - Count of datasets reprojected, unchanged, or assigned a spatial reference

## 📁 File Structure

```
BatchVerifyProjections/
├── BatchVerifyProjections.py    # Main script
├── instructions.md              # Assignment and setup instructions
└── README.md                    # You're here
```

## ⚙️ Requirements

- ArcGIS Pro with Python and `arcpy`
- Vector data in a geodatabase or shapefile format

## ⚠️ Error Handling

- Warnings for missing datasets or unknown spatial references.
- Errors are logged per dataset and summarized.
- Global error catch ensures graceful script termination.

## 📜 Version History

- **1.0** – Initial working version
- **1.1** – Converted input to `arcpy.GetParameterAsText`
- **1.2** – Integrated step progressor
- **1.3** – Dataset-level error handling
- **1.4** – Handled case with no vector datasets
- **1.5** – Global script error handling

## 🧾 License

This project is part of a lab assignment and is intended for educational use.
