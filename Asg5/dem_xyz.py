
# ====================================================
# Project Name: dem_xyz
# ====================================================
# Description:
#    This program will open a user speicified file DEM that has been saved in .xyz format. This will gather some metadata about the file and output it both to the user as well as to a file.
#    The metadata collected is the following:
#        1) How many UTM points there are
#        2) Minimum and Maximum easting values
#        3) Minimum and Maximum northing values
#        4) Approximate height of the tile
#        5) Approximate width of the tall
#        6) Minimum and Maximum elevation
#        7) Average elevation

# Author(s):
#    - Matt Findlay, matthew_findlay@ucalgary.ca
    
# Version:
#    1.0.0 - Initial creation of program. Opening a file and deteremine how many UTM points there are
#    1.1.0 - Added function definiton to gather important numbers from file
    
# Date:
#    2004-10-10
        
# Usage:
#    Provide a short example of how to use the code or a basic command to run the project.
    
# ====================================================

def gather_important_numbers(input_file):
    max_east = 0
    min_east = 0
    max_north = 0
    min_north = 0
    max_elevation = 0
    min_elevation = 0
    total_elevation = 0
    utm_points = sum(1 for line in input_file)
    
    
    for line in input_file:
        list_line = line.split()
        max_east = max(max_east, list_line[0])
        min_east = min(min_east, list_line[0])
        max_north = max(max_north, list_line[1])
        min_north = min(min_north, list_line[1])
        max_elevation = max(max_elevation, list_line[2])
        min_elevation = min_elevation(min_elevation, list_line[2])
        total_elevation += list_line[2]
    
    print(max_east)
    print(utm_points)
    
    return
    
        

file_name = input("Please input the name of the file you wish to open: ")



with open(file_name, 'r') as xyz_file:
    gather_important_numbers(xyz_file)
    
    
