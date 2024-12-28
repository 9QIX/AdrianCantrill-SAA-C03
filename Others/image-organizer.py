import os
import re
import shutil

# Regular expression to match the markdown image syntax
image_pattern = re.compile(r'!\[(.*?)\]\((.*?\.(?:png|jpg|jpeg|gif))\)')

# ANSI escape codes for colors and styles
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def ensure_images_directory(markdown_dir):
    """Creates an Images directory if it doesn't exist."""
    images_dir = os.path.join(markdown_dir, 'Images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        print(f"{GREEN}✔ Created Images directory: {images_dir}{RESET}")
    return images_dir

def move_image_to_images_folder(image_path, markdown_dir):
    """Moves an image file to the Images folder and returns the new path."""
    if not os.path.exists(image_path):
        print(f"{YELLOW}Warning: Image not found: {image_path}{RESET}")
        return None
        
    images_dir = ensure_images_directory(markdown_dir)
    image_filename = os.path.basename(image_path)
    new_image_path = os.path.join(images_dir, image_filename)
    
    # Move the file if it's not already in the Images directory
    if os.path.normpath(image_path) != os.path.normpath(new_image_path):
        try:
            shutil.move(image_path, new_image_path)
            print(f"{GREEN}✔ Moved image: {image_path} → {new_image_path}{RESET}")
        except Exception as e:
            print(f"{YELLOW}Warning: Could not move image {image_path}: {str(e)}{RESET}")
            return None
    
    return new_image_path

def modify_image_paths_in_markdown(file_path):
    """Reads and modifies image paths in a markdown file."""
    markdown_dir = os.path.dirname(file_path)
    changes_made = False
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all matches of image paths
    matches = image_pattern.findall(content)
    
    if matches:
        print(f"{CYAN}Processing: {file_path}{RESET}")
    
    def replace_func(match):
        nonlocal changes_made
        alt_text, old_image_path = match.groups()
        
        # Convert to proper path relative to markdown file
        if not old_image_path.startswith('./Images/'):
            # Handle absolute and relative paths
            full_image_path = os.path.join(markdown_dir, os.path.normpath(old_image_path))
            
            # Move the image file if it exists
            new_image_path = move_image_to_images_folder(full_image_path, markdown_dir)
            if new_image_path:
                # Convert to relative path with forward slashes
                relative_path = './Images/' + os.path.basename(new_image_path)
                changes_made = True
                print(f"{GREEN}✔ Updated path in markdown: {old_image_path} → {relative_path}{RESET}")
                return f'![{alt_text}]({relative_path})'
        
        return match.group(0)

    new_content = image_pattern.sub(replace_func, content)

    if changes_made:
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
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                modify_image_paths_in_markdown(file_path)
    print(f"{MAGENTA}Completed processing directory: {directory}{RESET}")

if __name__ == "__main__":
    # Use current directory as base directory
    base_dir = '../'
    process_directory(base_dir)