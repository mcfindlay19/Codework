import tkinter as tk
from tkinter import StringVar

# Function Definitions

# Update and write the output label based on input
def update_result(*args):
    try:
        # Grab the values from input boxes and convert them to float
        values = [float(num.get()) for num in numbers]
        
        # Latitude values [D, M, S]
        lat_values = values[0:3]
        # Longitude values [D, M, S]
        lon_values = values[3:6]
        
        # Convert DMS to decimal for latitude and longitude
        decimal_latitude = dms_to_decimal(lat_values)
        decimal_longitude = dms_to_decimal(lon_values)
        
        # Round off the floating point to 6 decimals
        decimal_latitude = round(decimal_latitude, 6)
        decimal_longitude = round(decimal_longitude, 6)
        
        # Display the result
        result_label.config(text=f"Coordinates in decimal degrees: {decimal_latitude}, {decimal_longitude}.")
    # Ensure only numbers are input    
    except ValueError:
        result_label.config(text="Invalid input.")

# Helper function to convert DMS to decimal degrees. This follows the algortihm laid out in mathworks dms2degrees
def dms_to_decimal(dms_values):
    sgn = 1  # Default sign is positive
    
    # Step 1: Determine the sign based on the first nonzero element
    for value in dms_values:
        if value != 0:
            if value < 0:
                sgn = -1  # Set the sign to negative if first nonzero is negative
            break
    
    # Step 2: Ensure no nonzero element is followed by a negative element
    nonzero_found = False
    for value in dms_values:
        if value != 0:
            if nonzero_found and value < 0:
                raise ValueError()
            nonzero_found = True
    
    # Step 3: Convert DMS to decimal using absolute values and apply the sign
    degrees, minutes, seconds = dms_values
    decimal = abs(degrees) + abs(minutes) / 60 + abs(seconds) / 3600
    return sgn * decimal

# Set up initial GUI window
root = tk.Tk()
root.title("Convert DMS to Decimal Degrees")
root.geometry("600x400")

# Variables to hold input numbers
numbers = [StringVar() for _ in range(6)]

# Labels for GUI
number_titles = ['Latitude Days: ', 'Latitude Minutes: ', 'Latitude Seconds: ', 'Longtitude Days: ', 'Longitude Minutes: ', 'Longitude Seconds: ']

# Setup input boxes with labels
for i in range(6):
    tk.Label(root, text=number_titles[i]).grid(row=i+2, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=numbers[i]).grid(row=i+2, column=1, padx=10, pady=5)

# Create output label and info
result_label = tk.Label(root, text="Please enter values above.")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

info_label1 = tk.Label(root,text="To use, ensure numbers are in each of the below boxes.")
info_label1.grid(row=0,column=0, columnspan=2, padx=10, pady=5)
info_label2 = tk.Label(root,text="Please enter negative numbers for coordinates south and west")
info_label2.grid(row=1,column=0, columnspan=2, padx=10, pady=5)

# This runs the update_result function whenever a value is changed in the input box, giving you real time info    
for num in numbers:
    num.trace_add("write", update_result)

# Run main TKInter loop
root.mainloop()