# 🛰️ GIS & Environmental Tools Suite

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/platform-ArcGIS--Pro%20%7C%20arcpy-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A collection of GIS, geoprocessing, and environmental analysis tools developed in Python and designed for ecological monitoring, spatial data standardization, and terrain analysis. These scripts automate common workflows and support academic and field-based research in geography and environmental science.

---

## Overview

- **Author:** Matt Findlay  
- **E-mail:** 
  - [matthew_findlay@ucalgary.ca](mailto:matthew_findlay@ucalgary.ca)
  - [mcfindlay19@gmail.com](mailto:mcfindlay19@gmail.com)
- **Location:** Calgary, Canada  
- **Version Date:** May 2025  
- **Latest Version:** 1.0.0  

---

## Features

- Vector projection validation and correction (NAD83 UTM Zone 12N)
- Wildlife survey file parsing and cleanup
- DEM metadata extraction and XYZ structure validation
- Batch geoprocessing utilities for shapefiles and feature classes
- Error-robust logging for batch workflows

---

## Installation

### Requirements

- Python 3.9+
- ArcGIS Pro with `arcpy`
- `pandas`, `os`, `datetime`, `logging`, `argparse`

### How to Clone

```bash
git clone https://github.com/mcfindlay19/Codework.git
cd Codework
```

### Setup

Ensure ArcGIS Pro is installed and that Python environment has access to `arcpy`.

### Configure Parameters

Each tool uses either command-line arguments or configurable variables in the script header.

### Run the Tool

- **Projection Checker:**  
  `python check_projections.py -w path/to/workspace`

- **Wildlife Survey Script:**  
  `python wildlife_cleaner.py`

- **DEM Metadata Extractor:**  
  `python dem_metadata_parser.py -f path/to/dem/file`

### Output

Each tool generates output reports (e.g., CSV summaries), projection logs, or corrected shapefiles in user-specified locations.

---

## File Structure

```
Codework/
│
├── projection_checker/
│   └── check_projections.py
│
├── wildlife_survey/
│   └── wildlife_cleaner.py
│
├── dem_tools/
│   ├── dem_metadata_parser.py
│   └── example_dem.xyz
│
├── README.md
└── LICENSE
```

---

## Error Handling

- Missing projections handled with warning and log output
- File parsing failures reported in a structured error log
- XYZ and DEM validators check header format and grid regularity

---

## Version History

- **v1.0.0** (May 2025): Initial release with core utilities
- **v0.9.0** (Nov-Dec 2024): Internal use

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

Thanks to University of Calgary's Geography department for foundational training and course integration. Built with tools used in GEOG 567, taught by the amazing Dr. Bender.
