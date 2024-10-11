
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
#    1.0.0 - Initial creation of program. Opening a file and determine how many UTM points there are
#    1.1.0 - Added function definiton to gather important numbers from file
#    1.1.1 - Documentation states that .xyz files should be int int float, but was instead formatted as float float float.
#    1.2.0 - Added writing to an output file
#    1.2.1 - Added writing output to the screen
#    1.3.0 - Added try block for opening file. Added docstrings
#    1.3.1 - Added more error handling, sepcifically for data inside file
    
# Date:
#    2004-10-10
        
# Usage:
#    Provide a short example of how to use the code or a basic command to run the project.
    
# ====================================================

def gather_important_numbers(input_file):
    """Gathers important metadata from a .xyz file"""
    # Initalize values to infinity or negative infinity
    max_east = float('-inf')
    min_east = float('inf')
    max_north = float('-inf')
    min_north = float('inf')
    max_elevation = float('-inf')
    min_elevation = float('inf')
    
    # Initalize other important values
    total_elevation = 0
    utm_points = 0
    
    # For every line inside the file, split the line into individual values
    for line in input_file.readlines():
        list_line = line.split()
        
        # Check to see if there are only 3 values per line
        if len(list_line) != 3:
            print(f"Warning: Invalid line format: {line.strip()}")
            continue
        
        # Check to ensure all values are valid inputs i.e. no letters or special characters
        try:
            easting = float(list_line[0])
            northing = float(list_line[1])
            elevation = float(list_line[2])
        except ValueError:
            print(f"Warning: Invalid numeric values in line: {line.strip()}")
            continue
        
        # See if the values are a new max or a new min
        max_east = max(max_east, easting)
        min_east = min(min_east, easting)
        max_north = max(max_north, northing)
        min_north = min(min_north, northing)
        max_elevation = max(max_elevation, elevation)
        min_elevation = min(min_elevation, elevation)
        
        # Sum all elevation data to be able to calculate the average
        total_elevation += elevation
        
        #Keep track of how many points there are
        utm_points += 1
    
    return utm_points, max_east, min_east, max_north, min_north, max_elevation, min_elevation, round(total_elevation/utm_points, 4)
        
def print_output(utm_points, max_east, min_east, width, max_north, min_north, height, max_elevation, min_elevation, average_elevation):
    # Prints the output results to the console
    """Prints the output results to the console"""
    print(f"There are {utm_points} UTM points.\n")
    print(f"The maximum easting is {max_east} meters east.\n")
    print(f"The minimum easting is {min_east} meters east.\n")
    print(f"The width of the area is {width} meters.\n")
    print(f"The maximum northing is {max_north} meters north.\n")
    print(f"The minimum northing is {min_north} meters north.\n")
    print(f"The height of the area is {height} meters.\n")
    print(f"The max elevation is {max_elevation} meters.\n")
    print(f"The minimum elevation is {min_elevation} meters.\n")
    print(f"The average elevation is {average_elevation} meters.\n")
    
    pass

file_name = input("Please input the name of the file you wish to open: ")
text_name = file_name.split('.')[0] + '.txt'


try:
    
    with open(file_name, 'r') as xyz_file:
        utm_points, max_east, min_east, max_north, min_north, max_elevation, min_elevation, average_elevation = gather_important_numbers(xyz_file)
        
    width = max_east - min_east
    height = max_north - min_north

    with open(text_name, 'w') as txt_file:
        txt_file.write(f"There are {utm_points} UTM points.\n")
        txt_file.write(f"The maximum easting is {max_east} meters east.\n")
        txt_file.write(f"The minimum easting is {min_east} meters east.\n")
        txt_file.write(f"The width of the area is {width} meters.\n")
        txt_file.write(f"The maximum northing is {max_north} meters north.\n")
        txt_file.write(f"The minimum northing is {min_north} meters north.\n")
        txt_file.write(f"The height of the area is {height} meters.\n")
        txt_file.write(f"The max elevation is {max_elevation} meters.\n")
        txt_file.write(f"The minimum elevation is {min_elevation} meters.\n")
        txt_file.write(f"The average elevation is {average_elevation} meters.\n")

    print_output(utm_points, max_east, min_east, width, max_north, min_north, height, max_elevation, min_elevation, average_elevation)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Program is quitting.")