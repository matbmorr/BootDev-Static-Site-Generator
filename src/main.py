import os
import shutil
from page_generation import generate_pages_recursive

def copy_directory(source, destination):
    # First ensure the destination is clean
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    # Create the destination directory
    os.mkdir(destination)
    
    # Get list of all items in the source directory
    items = os.listdir(source)
    
    # Loop through each item
    for item in items:
        # Create full paths
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        
        # Check if it's a file or directory
        if os.path.isfile(source_path):
            # It's a file - copy it
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {source_path} to {destination_path}")
        else:
            # It's a directory - recursively copy it
            copy_directory(source_path, destination_path)
            print(f"Copied directory: {source_path} to {destination_path}")

def main():
    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    
if __name__ == "__main__":
    main()