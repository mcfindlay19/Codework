PROJECT: Create a Script to Input LiDAR 15 ASCII Raster Tiles 

 

In this lab assignment, you will be working with Python to input LiDAR
15 digital elevation model (DEM) files that can be obtained from the
provincial DEM database distributed by AltaLIS
( [http://www.altalis.com](http://www.altalis.com/)). The UofC Library's
Spatial and Numerical Data Services maintains access to the entire
provincial LiDAR 15 DEM database for academic use, and the products can
be purchased from AltaLIS for commercial use. However, the LiDAR15 DEM
data for this lab is also provided by AltaLIS through the Open Data
Areas Alberta project
([http://opendataareas.ca](http://opendataareas.ca/)). The specific
format we will work with is the LiDAR15 'XYZ' format. Your first step
will be to download the LiDAR15 XYZ data files from their website,
inspect the structure and content of the data files, and familiarize
yourself with the LiDAR15 metadata document.   

  

This lab will have you working with text files, which we studied last
week, as well as practice working with Python functions to manipulate
numbers and strings. 

  

A. Download the Data 

Go to the Open Data Areas Alberta project website
at [http://opendataareas.ca](http://opendataareas.ca/) and search for
the **LiDAR15 DEM** dataset for Taber, Alberta. If you search using the
terms LiDAR15 and Taber, you should easily find it. Read the metadata
summary on the website to be sure you are downloading the correct
product (make sure you have the ASCII format files in the UTM
projection). Also, be sure to view the data license before downloading
the data.  

 

Once you understand the use limitations, download the data to your
computer -- you should now have a file
called **Taber_LiDAR15_DEM_Altalis.zip**. Unzip the file and inspect the
contents. There should be a number of .xyz files (those are the DEM's in
ASCII text format), as well as a PDF file that contains the metadata. 

  

The .xyz files contain the DEM data, and the structure is explained in
the accompanying metadata document (**LiDAR15 DEM.pdf**). The .xyz files
are a proprietary format used for LiDAR DEM data, and like many DEM file
formats, the data are stored in easily-readable text files. To view the
contents, you can open the files in a text editor, such as Notepad or
Notepad++.  

  

Have a look at the contents of one of the .xyz files in a text editor,
and examine the metadata document to get a feel for what information is
stored in each xyz file. Essentially, each row of the file contains a
UTM coordinate with an elevation corresponding to a single point
location. There are numerous points in the file, which correspond to a
grid-like lattice of points that define the heights of a specified
region (much like pixels on a raster grid). In the sample file you have
downloaded, the point spacing is 15 m and the approximate dimension of
each rectangular tile is about 10 x 10 km. However, tile size is not
necessarily consistent for each .xyz file. 

** ** 

B. Process the Data in Python 

Your main task in this lab assignment is to create a Python script that
will read a LiDAR15 ASCII format DEM file (i.e., .xyz file) and extract
some metadata information. Specifically, your script must accomplish the
following: 

1.  Prompt the user to input the name of a LiDAR15 .xyz tile (e.g.,
    414019_A.xyz). 

2.  Determine how many UTM points are in the tile. 

3.  Determine the minimum and maximum easting values. 

4.  Determine the minimum and maximum northing values. 

5.  Determine the approximate height (north to south) of the tile in
    km. 

6.  Determine the approximate width (east to west) of the tile in km. 

7.  Determine the minimum and maximum elevation value in the tile. 

8.  Determine the average (mean) elevation in the tile. 

9.  Output the results to the user in an informative and aesthetically
    pleasing manner. 

10. BONUS (optional): For 5 bonus marks (not to exceed 100% overall),
    output your results to the user to both the screen as well as a new
    text file that is created in the same folder as your .xyz file. The
    output file should have the same file name as the input, but it
    should have a .txt file extension instead (e.g., 414019_A.txt). 
