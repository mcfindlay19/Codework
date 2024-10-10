file_name = input("PLease input the name of the file you wish to open")

with open(file_name, 'r') as xyz_file:
    line_count = sum(1 for line in xyz_file)
    
print(line_count)