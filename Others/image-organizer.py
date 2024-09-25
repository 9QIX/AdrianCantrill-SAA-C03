import os
import re

# Regular expression to match the markdown image syntax
image_pattern = re.compile(r'!\[(.*?)\]\((image(?:-\d+)?\.png)\)')

# Base directory where you want to start the search
base_dir = '../'  # Current directory

# ANSI escape codes for colors and styles
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def modify_image_paths_in_markdown(file_path):
    """Reads and modifies image paths in a markdown file."""
    changes_made = False
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all matches of image paths
    matches = image_pattern.findall(content)
    
    if matches:
        print(f"{CYAN}Processing: {file_path}{RESET}")
    
    # Replace image paths if they don't already contain "./Images/"
    def replace_func(match):
        nonlocal changes_made
        old_image_path = match[1]
        new_image_path = f"./Images/{old_image_path}"
        
        if not match[1].startswith('./Images/'):
            print(f"{GREEN}✔ Changed: {YELLOW}{old_image_path} {RESET}→ {YELLOW}{new_image_path}{RESET}")
            changes_made = True
            return f'![{match[0]}]({new_image_path})'
        return match[0]

    new_content = image_pattern.sub(replace_func, content)

    if changes_made:
        # Save the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"{GREEN}✔ File updated: {file_path}{RESET}\n")
    else:
        print(f"{YELLOW}No changes needed: {file_path}{RESET}\n")

def process_directory(directory):
    """Recursively processes all markdown files in a directory."""
    print(f"{MAGENTA}Starting search in directory: {directory}{RESET}\n")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                modify_image_paths_in_markdown(file_path)
    print(f"{MAGENTA}Completed processing directory: {directory}{RESET}")

if __name__ == "__main__":
    # Start processing from the base directory
    process_directory(base_dir)
