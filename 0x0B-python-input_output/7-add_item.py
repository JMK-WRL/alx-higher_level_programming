#!/usr/bin/python3
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Check if the add_item.json file exists
if os.path.exists("add_item.json"):
    # Load the existing list from the file
    my_list = load_from_json_file("add_item.json")
else:
    # Create a new empty list if the file doesn't exist
    my_list = []

# Add command-line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the add_item.json file
save_to_json_file(my_list, "add_item.json")
