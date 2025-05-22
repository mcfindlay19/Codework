# Topographic Roughness Index (TRI) Computation Tool

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/platform-ArcGIS--Pro%20%7C%20arcpy-orange)

## Overview

- **Author:** Matt Findlay  
- **E-mail:** 
 - [matthew_findlay@ucalgary.ca](mailto:matthew_findlay@ucalgary.ca)
 - [mcfindlay19@gmail.com](mailto:mcfindlay19@gmail.com)
- **Date of version:** Feb 4, 2025  
- **Latest version:** 1.0  

This script calculates the Topographic Roughness Index (TRI) for a given DEM using map algebra and focal statistics. It is designed to run within the ArcGIS Pro Python environment and outputs the TRI raster in a designated output folder.

## Features

- Calculates TRI using an efficient map algebra approximation.
- Uses 3x3 window focal statistics to determine elevation variability.
- Automatically manages output folder creation and file saving.
- Intermediate files are cleaned up to conserve disk space.
- Handles errors gracefully with try-except logic.

## Installation

### Requirements

- ArcGIS Pro with Spatial Analyst extension
- Python environment compatible with arcpy
- A raster DEM file (GeoTIFF or similar format)

### How to Clone

```bash
   git clone https://github.com/mcfindlay19/Codework.git
   cd week11
   ```

### Setup

1. Ensure ArcGIS Pro is installed with the Spatial Analyst license enabled.
2. Place the script `tri.py` in your desired workspace.
3. Ensure your DEM raster file is accessible.

### Configure Parameters

- The script takes a single input parameter: the path to your DEM raster.

### Run the Tool

You can run the script directly from the ArcGIS Pro Python environment:

```python
input_dem = "C:/path/to/your/dem.tif"
compute_tri(input_dem)
```

Or use it as a custom script tool in ArcGIS by linking `tri.py` to a `.tbx` toolbox.

### Output

- TRI raster file named `<input_name>_tri.tif` saved in an `output` directory created next to the input DEM.

## File Structure

```
tri.py
instructions.md
/output/
    ├── <input_name>_tri.tif
```

## Error Handling

The script includes:
- Checks for valid input file
- Creation of output directory if not present
- Try-except block to catch and print runtime errors
- Cleanup of intermediate rasters (`D2.tif`, `F1.tif`, `F2.tif`)

## Version History

- **v1.0** (Feb 4, 2025): Initial implementation of TRI computation using map algebra.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
