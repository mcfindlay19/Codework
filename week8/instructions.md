PROJECT: Create a Geoprocessing Script Using Python 

  

This week you will create your first Python script to work with GIS
data. Design a script to search a workspace containing vector GIS
datasets (i.e. a location to store feature classes, such as shapefiles
or geodatabase feature classes), check if they area all using the same
spatial reference system (NAD83 UTM Zone 12N), and if not correct this,
and then output some information to the user.  \
 

These are the steps: 

  

- prompt the user to input a path to a workspace location containing GIS
  datasets (for this assignment, assume the user will enter the path
  correctly for Python to interpret it without error) 

  - note: the workspace could be a folder (for shapefiles) or
    geodatabase (for feature classes), and the script must handle both
    cases 

  - sample data are provided in the attached file
    called sample_data.zip \
     

- use arcpy to obtain a list of all vector datasets (i.e., shapefiles or
  geodatabase feature classes) in the workspace  \
   

- inspect each vector dataset within the folder to ensure they are all
  using the same spatial reference system, namely NAD 1983 UTM Zone 12N
  (EPSG/WKID: 26912) 

  - if a dataset does not have a spatial reference system defined, you
    can safely assume it is in geographic coordinates (NAD 1983 datum);
    use the Define Projection tool programmatically to assign this
    coordinate system to the dataset  

    - hint: the **name** property of the SpatialReference object will be
      "Unknown" if the spatial reference system has not been defined for
      the dataset 

    - remember: datasets in geographic coordinates will later need to be
      projected to the UTM PCS -- see the last bullet below 

  - if a dataset has a spatial reference system attached, assess whether
    it is the correct one (i.e., is it NAD83 UTM 12N?) 

    - if it is correct, nothing else is required 

  - for all datasets not in NAD83 UTM 12N (including the ones you
    defined as GCS NAD83 above), use the Project tool to transform it to
    the correct spatial reference system (be sure to retain the original
    name of the shapefile) 

    - hint: the Project tool may or may not allow you to overwrite an
      existing file, so you may have to design some logic to overcome
      this \
       

- finally, output the following information to the user: 

  - the total number of vector datasets, overall 

    - a breakdown of the number of shapefiles by geometry shape type 

    - e.g., how many polygon shapefiles, how many point shapefiles,
      etc. 

  - the number of datasets in each of the following categories: 

    - number that were already in the NAD83 UTM 12N PCS 

    - number that were in another spatial reference (e.g., GCS or
      different datum) 

    - number of datasets that had no spatial reference information 

  - report the names (if any) of the vector datasets that did not have
    spatial reference defined 

 

Assumptions 

  

- Assume that the user of your script will correctly enter in the full
  path to the workspace location on a Windows PC (e.g.,
  \'C:\\GIS\\Lab8\\MyData.gdb\').  

- Unless a spatial reference system is already defined for a vector
  dataset, assume that your data are in geographic coordinates using the
  North American 1983 datum (i.e., spatial reference system =
  GCS_North_American_1983; EPSG/WKID: 4269). 
