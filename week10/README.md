# Wildlife Survey Data Import & Analysis

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Platform](https://img.shields.io/badge/platform-ArcGIS--Pro%20%7C%20arcpy-orange)

A custom ArcGIS Pro geoprocessing script tool for importing wildlife survey CSV data, converting coordinates, and identifying extreme geographical locations where species presence is observed.

---

## Overview

- **Author:** Matt Findlay  
- **E-mail:** 
  - [matthew_findlay@ucalgary.ca](mailto:matthew_findlay@ucalgary.ca)
  - [mcfindlay19@gmail.com](mailto:mcfindlay19@gmail.com)
- **Date of Version:** February 3, 2025  
- **Latest Version:** v1.4  

---

## Features

- Converts DMS coordinates to Decimal Degrees.
- Imports CSV as a geospatial point feature class in ArcGIS Pro.
- Retains original survey attributes.
- Performs analysis to find:
  - Total number of positive species presence records.
  - 3 most northern, southern, eastern, and western records.
- Outputs findings in ArcGIS Pro Messages pane.
- Robust error handling.

---

## Installation

### Requirements

- ArcGIS Pro (with `arcpy`)
- Python 3.x (via ArcGIS)
- CSV file formatted with fields:
  - Year, SurveyID, Presence, sLatitude, sLongitude

### How to Clone
   ```bash
   git clone https://github.com/mcfindlay19/Codework.git
   cd week10
   ```

### Setup

1. Open ArcGIS Pro.
2. Add the script as a script tool in a custom toolbox.
3. Ensure permissions to read CSVs and write to a geodatabase.

### Configure Parameters

- **Input:** CSV file path (e.g., `data/survey.csv`)
- **Output:** Path to desired feature class (e.g., `Database.gdb/SurveyPoints`)

### Run the Tool

Execute via the ArcGIS Pro toolbox or Python toolbox interface.

### Output

- Feature class containing survey points.
- Message pane logs species presence stats and extreme coordinates.

---

## File Structure

```
wildlife-survey-import/
│
├── wildlife.py           # Main script tool
├── instructions.md       # Assignment description
├── FlowChart.png         # Workflow diagram
└── README.md             # This file
```

---

## Error Handling

- Uses `try/except` blocks for:
  - Coordinate conversion
  - CSV row validation
  - Feature class creation
- Skips malformed rows with warnings.
- Graceful exit with user feedback on fatal errors.

---

## Version History

- **v1.0** – Initial script implementation  
- **v1.1** – Fixed missing point geometry issue  
- **v1.2** – Corrected east-west mirroring of coordinates  
- **v1.3** – Improved error handling and validation  
- **v1.4** – Final testing and optimization  

---

## License

[MIT License](https://opensource.org/licenses/MIT)
