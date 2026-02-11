import os

# specify directory (empty string means current directory)
directory = "/"

# list and print
for item in os.listdir(directory):
    print(item)
