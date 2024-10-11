
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
#    1.1.0 - Documentation states that .xyz files should be int int float, but was instead formatted as float float float. 
    
# Date:
#    2004-10-10
        
# Usage:
#    Provide a short example of how to use the code or a basic command to run the project.
    
# ====================================================

def gather_important_numbers(input_file):
    # Initilize values to infinity or negative infinity
    max_east = float('-inf')
    min_east = float('inf')
    max_north = float('-inf')
    min_north = float('inf')
    max_elevation = float('-inf')
    min_elevation = float('inf')
    # Initilize other important values
    total_elevation = 0
    utm_points = 0
    
    
    for line in input_file.readlines():
        list_line = line.split()
        max_east = max(max_east, float(list_line[0]))
        min_east = min(min_east, float(list_line[0]))
        max_north = max(max_north, float(list_line[1]))
        min_north = min(min_north, float(list_line[1]))
        max_elevation = max(max_elevation, float(list_line[2]))
        min_elevation = min(min_elevation, float(list_line[2]))
        total_elevation += float(list_line[2])
        utm_points += 1
    
    return utm_points, max_east, min_east, max_north, min_north, max_elevation, min_elevation, total_elevation/utm_points
        
def print_output(utm_points):
    
    pass

file_name = input("Please input the name of the file you wish to open: ")
text_name = file_name.split('.')[0] + '.txt'


with open(file_name, 'r') as xyz_file:
    utm_points, max_east, min_east, max_north, min_north, max_elevation, min_elevation, average_elevation = gather_important_numbers(xyz_file)
    
width = max_east - min_east
height = max_north - min_north

with open(text_name, 'w') as txt_file:
    txt_file.write(f"There are {utm_points} UTM points\n")
    txt_file.write(f"The maximum easting is {max_east} meters east\n")
    txt_file.write(f"The minimum easting is {min_east} meteres east\n")
    txt_file.write(f"The width of the area is {width} meters\n")
    txt_file.write(f"The maximum northing is {max_north} meters north\n")
    txt_file.write(f"The minimum northing is {min_north} meters north\n")
    txt_file.write(f"The height of the area is {height} meters\n")
    txt_file.write(f"The max elevation is {max_elevation} meters\n")
    txt_file.write(f"The minimum elevation is {min_elevation} meters\n")
    txt_file.write(f"The average elevation is {average_elevation} meters\n")
