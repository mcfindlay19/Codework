PROJECT: Creating Script Tools in ArcGIS 

   

In this week\'s assignment, you will reuse the batch processing script
that you created last week and convert it into a script tool that can be
executed in ArcGIS. You will also add a step progressor so that the user
can track the progress of the script as it executes, and you will add
some Python error checking functionality. 

 

Since you have already designed and coded the batch processing script
last week, you are [not]{.underline} required to submit any of the steps
in the Program Development Cycle for this assignment. You will be
modifying your code (see below), but we will assume that the basic logic
of your script will not change. 

  

Create a Custom Toolbox and New Script Tool 

  

Your first task is to create a custom toolbox (\*.atbx file) that you
will use to store your script tools. Do not confuse custom toolboxes
with Python toolboxes -- a custom toolbox can be created simply by going
into Catalog, right-clicking any folder on your computer, and selecting
New 🡪 Toolbox, and it is ready to go. Python Toolboxes require many
more steps before they can be used, and we will not learn to create them
in this course (but once you have mastered basic Script Tools inside
custom toolboxes, you may want to explore Python toolboxes and Python
function tools because they offer greater power and flexibility). 

  

To begin, please complete the following: 

   

- In a folder that you will remember, use Catalog to create a new custom
  toolbox, and give it the name \<*Lastname*\>\_Lab9.atbx (e.g.,
  Bender_Lab9.atbx).  

- Once the custom toolbox has been created, right-click the toolbox and
  select Add 🡪 Script to create a script tool.  

  - Give it the name \"BatchVerifyProjections\" (you may not use spaces
    or underscore characters). You will use this name to refer to the
    tool in your Python code. 

  - Give it the label \"Batch Verify Projections\" (this is the
    \'alias\' name for the tool, which is what you will see as the
    tool\'s label in Toolbox). 

  - Accept all the defaults and complete the wizard to create the script
    tool. It should now be visible in your custom toolbox. 

 

Now that you have your script tool created, you can right-click it in
Catalog and choose Properties to modify it at any time. 

 

Program the Script Tool 

 

1.  Your first task is to modify your script from your Week 8 Lab
    Assignment into a script tool that will allow the user to input the
    following: 

    - the workspace containing vector datasets 

    - the spatial reference system that should be used to define the
      spatial reference system for any vector datasets that do not have
      one defined \
       

Thus, you will need to add two parameters to your script tool. The first
parameter should be labelled \"Input Workspace or Feature Dataset\"
(workspaces and feature datasets are both valid containers for storing
vector datasets) and the second parameter should be labelled \"Spatial
Reference System\".  \
  

2.  You must also set an expected data type or object type for each
    parameter in the tool. In the properties dialog for the script tool,
    there is a drop-down list that you can select your parameters\' data
    types. Think carefully about what is needed here, and choose
    something appropriate for each parameter. \
     

3.  Now you can make a copy of your script from Lab 8 and put it into
    the same folder where you stored your script tool (this is the
    safest method). Modify your script in two ways: \
     

    a.  User input will be accomplished through the script tool you just
        parameterized, so we no longer wish to prompt the user to enter
        a workspace using the input() function. Instead, use
        the arcpy.GetParameterAsText() function to obtain a workspace
        location. Modify your script accordingly. \
         

    b.  Allow the user to select any spatial reference system for your
        tool. In Lab 8, you hard-coded in a particular spatial reference
        system, but this tool will be more functional. Modify your
        script to obtain the spatial reference system from the script
        tool at run-time, and remove references to the spatial reference
        system you used in Lab 8. \
         

4.  Once you have modified your code, you can associate your script as
    the Source code in the script tool\'s Properties Dialog. Make sure
    that you enable the option for the tool to use relative path names
    to your script (otherwise, your tool will not run when we evaluate
    it!). \
     

5.  Test out your script to see if it works. If not, review the steps
    above to see if there is anything you missed. Note: you are not
    required to add Validation or Help properties to your script tool. \
     

6.  Once your script is functioning properly, add a Step Progressor into
    the code to inform the user about the progress of the batch
    processing operation. Also output any relevant messages arising from
    the execution of any geoprocessing tools. Consult the lecture
    materials if you are unsure what to do here. \
     

7.  Finally, where appropriate, add at least one Python error handling
    routine to capture an unexpected error and output some form of
    message to the tool. \
     

Document Your Code 

  

Once you have completed your script tool and It is executing as you
intend, please go back and fully document your Python code. You should
provide proper header documentation, as well as embedded comments that
sufficiently explain each step of the script\'s operation. 
