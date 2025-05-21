PROJECT: Performing Raster Calculations with Map Algebra 

 

In this week\'s assignment, you will be working with raster datasets and
arcpy scripts to perform map algebra calculations. Map algebra
calculations, such as those that you can perform with the Raster
Calculator, represent an extremely powerful toolset for spatial
analysis. However, performing complex computations through the Raster
Calculator GUI can be very cumbersome, and having to repeat the same
workflow over and over is time consuming and often leads to user
errors. 

  

Scripting these operations is surprisingly easy in arcpy, especially
when using the arcpy.sa (Spatial Analyst) module, which streamlines map
algebra computations by providing a straightforward syntax for
performing calculations that his remarkably similar to working with
scalar values (i.e., normal math calculations). For example, to compute
the arithmetic mean of three input raster layers, all one has to do is
instantiate Raster objects to represent each input dataset and then use
a simple formula (see the last line in the example script below). 

  

Example: 

  

import arcpy 

from arcpy.sa import \* 

f1 = Raster(\'C:\\Rasters\\factor1.tif\') 

f2 = Raster(\'C:\\Rasters\\factor2.tif\') 

f3 = Raster(\'C:\\Rasters\\factor3.tif\') 

out_raster = (f1 + f2 + f3) / 3 

** ** 

Creating Surface Analysis Tools 

  

In this week\'s lab, you will create a custom script tool that performs
a type of surface analysis called the topographic roughness index (TRI),
which quantifies the amount of local relief across a region. Various
forms of topographic roughness, also called terrain ruggedness, exist.
One of the most commonly used indices for TRI was published by [Riley
et. al
(1999)](https://www.researchgate.net/publication/259011943_A_Terrain_Ruggedness_Index_that_Quantifies_Topographic_Heterogeneity),
which is available for [ArcGIS Pro in the ArcHydro Tools Pro
toolset](https://community.esri.com/t5/water-resources-blog/terrain-ruggedness-index-tri-and-vector-ruggedness-measurement/ba-p/884340),
which is free to download and install.  

  

Most TRI computations calculate the amount of relief (difference in
elevation) in a moving-window operation across an entire DEM. A common
method is to use a 3x3 moving window to compare the height of the focal
pixel to its eight neighbours. The typical approach is to compute the
average squared difference of the focal cell to its neighbours, and then
take the square root of this value to obtain a single measure of
topographic heterogeneity within the window (i.e., somewhat similar to a
spatial variance metric). The moving-window operation is then repeated
across the entire DEM to map TRI. Riley et al\'s (1999) algorithm
follows such an approach, but it is slow because it must make
cell-by-cell computations. 

  

Evans et al (2014) have proposed a map algebra alternative that
approximates the same cell-by-cell computation but can be computed much
more efficiently. Their approximation method requires the following
inputs:  

1.  A raster DEM (we will use one of the LiDAR15 datasets that you
    worked with in Lab #5; call this **D1**) 

2.  A raster of the squared DEM values (**D2**) 

3.  Focal statistics rasters for the sum of DEM values within a 3x3
    window (**F1**) and sum of the squared DEM values in a 3x3 window
    (**F2**) 

  

Here is the pseudocode for their algorithm to approximate TRI: 

- create a raster layer of squared elevation values from the input DEM
  (i.e., DEM \* DEM) (**D2**) 

- use the [FocalStatistics tool in Spatial
  Analyst](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/focal-statistics.htm) to
  compute the sum of elevation pixels using a 3x3 window across the
  input DEM raster (F1) 

  - ensure that you use the NODATA option or you may get outrageous
    values! 

- use the FocalStatistics tool in Spatial Analyst to compute the sum of
  squared elevation pixels using a 3x3 window across the squared DEM
  raster (F2) 

  - ensure that you use the NODATA option! 

- user map algebra to compute TRI as:   

> TRI = SquareRoot(2 + F2 + 9\*D2 - 2\*D1\*F1) 

  

(Note: for those who are interested, Bill Huber has explained this
procedure very well in a GIS Stack Exchange post
at: <https://gis.stackexchange.com/questions/6056/calculating-topographic-ruggedness-index-in-arcgis-desktop>). 

  

**Your task for this lab is to create a custom script tool that computes
this quick version of TRI**. This is a great example of using Python to
extend the capabilities of ArcGIS by creating new, custom tools or
functionality that aren\'t built-in to the software. 

  

Steps to Accomplish the Task 

    

Here are the steps you should follow to achieve this task: 

1.  Create a Python script that inputs a raster DEM (D1). There are
    sample DEM files (geotiffs) provided as an attachment to this
    assignment in D2L. These are the same provincial LiDAR15 DEMs that
    you worked with in Lab 5, but they have been converted from an XYZ
    to TIF format for you. 

2.  Perform the calculations from the pseudocode above: 

    a.  Use map algebra and the Focal Statistics tool in ArcGIS to
        compute D2, F1, and F2. 

    b.  Use map algebra to apply the TRI formula in your script and
        create the output TRI raster. 

    c.  Ensure the TRI raster is saved as a permanent dataset. 

    d.  If necessary, delete the intermediate rasters D2, F1, F2 as they
        are no longer needed. (If you created these as temporary
        datasets, Spatial Analyst should clean  them up for you
        automatically.) 

3.  Once your script is running as expected and you have tested that it
    is fairly robust (you will want to add some error checking
    routines/try-except blocks to handle run-time errors), then convert
    the script to an ArcGIS custom script tool. 

    a.  The tool should prompt the user to enter an input raster dataset
        (the DEM) and provide an output name/location for the TRI
        dataset produced by the tool. 

    b.  The tool should be embedded within a custom toolbox (.tbx) file
        for submission, and the associated .py file should be made
        available with the tool. 

4.  Document your code thoroughly. At a minimum, you should provide
    header documentation and sufficient inline documentation for the
    reader to understand your script tool\'s operation. 
