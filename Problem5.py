import os  # Import the os module to work with directories

path = "/"  # Set the directory path (current directory)

files = os.listdir(path)  # Get a list of all files and folders in the directory

for file in files:  # Loop through and print each item
    print(file)
