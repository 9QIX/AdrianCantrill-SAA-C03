import os
import re

# Regular expression to match the markdown image syntax
image_pattern = re.compile(r'!\[(.*?)\]\((image(?:-\d+)?\.png)\)')

# Base directory where you want to start the search
base_dir = '../'  # Current directory

def modify_image_paths_in_markdown(file_path):
    """Reads and modifies image paths in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace image paths if they don't already contain "./Images/"
    new_content = image_pattern.sub(r'![\1](./Images/\2)', content)

    if new_content != content:
        # Save the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Modified: {file_path}")
    else:
        print(f"No changes needed: {file_path}")

def process_directory(directory):
    """Recursively processes all markdown files in a directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                modify_image_paths_in_markdown(file_path)

if __name__ == "__main__":
    # Start processing from the base directory
    process_directory(base_dir)
