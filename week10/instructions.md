PROJECT: Working with Vector Data in Arcpy Using Cursors 

   

In this week\'s assignment, you will be working with tabular and vector
datasets using cursors and arcpy's Data Access (arcpy.da) module.
Cursors are the main tool that we use to work with both standalone
tables and feature classes in ArcGIS. 

  

Your task this week is to create a custom tool in ArcGIS Pro that will
import tabular data stored as a CSV file. The CSV table was created by a
hypothetical database application that is used to record an annual
wildlife survey in North America for a rare species of bird. Each row in
the table represents a survey location that is visited annually. The
table contains fields for the year of survey, the survey location id
(unique key), and whether the species was present or not (1 = present, 0
= absent) at the time of the survey. Location coordinates are stored as
latitude-longitude values, but unfortunately, these values are stored in
an unconventional format that the GIS cannot easily read. The first few
rows of the CSV table are shown below so that you can see what this
looks like: 

  

  -------------------------------------------------------------------------------------
   **Year**    **SurveyID**    **Presence**   **sLatitude**       **sLongitude** 
  ----------- --------------- --------------- ------------------- ---------------------
     2022         102001            1         47D-27M-56.38S      124D-16M-54.81S 

     2022         102002            0         38D-19M-20.55S      105D-30M-24.85S 

     2022         102003            1         40D-16M-14.50S      107D-51M-26.20S 

     2022         102004            1         41D-29M-49.86S      107D-54M-40.44S 

     2022         102005            0         39D-31M-14.51S      106D-25M-18.98S 
  -------------------------------------------------------------------------------------

  

You will design a script tool using Python code that will input the CSV
file and output a point feature class with all the attribute fields
above (retain the original sLatitude and sLongitude fields that you see
above).  

  

Since you have already designed and coded a script in Lab 4 to handle
the conversion of coordinates from DMS format to DD, feel free to reuse
that code in this assignment. If you do, you
are [not]{.underline} required to submit pseudocode, flowcharts, testing
or debugging information associated with the DMS to DD portion of your
code. 

** ** 

Tool Requirements 

     

The script tool you create must satisfy the following: 

  

- Prompt the user to identify an input CSV file that contains data
  similar to the **routes.csv** file attached to your assignment (all
  years share exactly the same format, so your tool should work with any
  CSV table from any year, and not just the one provided). You should
  also prompt the user to specify the output feature class name and
  location. 

- ArcGIS can read CSV files but it cannot modify them, so you may wish
  to import the CSV file as a standalone table in your project\'s
  geodatabase. 

- Your script should interpret the information in the table to construct
  the attribute fields in the output feature class (assume the field
  SurveyID is always an integer number and the coordinates in the table
  use the WGS 1984 datum). 

- Your script must be capable of determining the latitude and longitude
  from the CSV table for each row, so you will have to come up with an
  algorithm to extract the degrees minutes and seconds values from the
  text-based coordinates. Then you can use your DMS converter function
  to turn these into decimal degrees values. 

- The output of the tool will be a point feature class where each row of
  the table will become a point feature. Ensure you preserve all the
  fields from the original table as attributes in your output feature
  class. 

- You can choose how you want to create the output feature class, and
  you will have to design a geoprocessing workflow to achieve this. For
  example, one method would be to  add two new fields to store the
  decimal degrees values for the latitude and longitude values of each
  coordinate in the table, then convert the DMS values into DD values
  and store them in the table, then use the Make XY Event Layer tool to
  generate a point feature class. You don't have to use this method, but
  you are welcome to adapt this workflow. Remember to show the steps
  explicitly in your flowchart. 

- To practice working with cursors, you will also have to use a search
  cursor to scan the [feature class]{.underline} you created (not the
  CSV table) to gather the following statistics and output them to the
  user as part of the script tool's operation: 

  - Total number of survey locations at which the species was present. 

  - The SurveyIDs and coordinates of the three most northern and three
    most southern observations of the species (note: an observation is
    indicated as Presence = 1). 

  - The SurveyIDs and coordinates of the three furthest west and three
    furthest east observations of the species. 

- Remember that your output information must be displayed in the
  Messages pane generated by the tool (print statements won't work with
  script tools). 

- Include error checking where appropriate. You must include at least
  one try/except block in your code and use it in
  an [appropriate]{.underline} way (don\'t embed your main body of the
  script it one huge try block!!). 

- You are [not]{.underline} required to use a progressor for this script
  -- the script will likely execute very quickly and this is not a batch
  processing script that will consume a lot of time, so there is no need
  to a progressor to your script tool unless you want to practice.  
