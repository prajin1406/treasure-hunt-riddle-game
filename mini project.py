import os
import shutil

Define file type categories

FILE_CATEGORIES = {
"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
"Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
"Videos": [".mp4", ".mkv", ".mov", ".avi"],
"Music": [".mp3", ".wav", ".aac"],
"Archives": [".zip", ".rar", ".tar", ".gz"],
"Scripts": [".py", ".js", ".html", ".css"],
"Others": []
}

def get_category(extension):
"""Return folder name based on file extension."""
for category, extensions in FILE_CATEGORIES.items():
if extension.lower() in extensions:
return category
return "Others"

def organize_files(directory):
"""Organize files in the given directory."""
if not os.path.exists(directory):
print(f"Directory does not exist: {directory}")
return

for filename in os.listdir(directory):  
    file_path = os.path.join(directory, filename)  

    # Skip directories  
    if os.path.isdir(file_path):  
        continue  

    _, extension = os.path.splitext(filename)  
    category = get_category(extension)  

    # Create category folder if it doesn't exist  
    category_folder = os.path.join(directory, category)  
    os.makedirs(category_folder, exist_ok=True)  

    # Move file  
    destination = os.path.join(category_folder, filename)  

    try:  
        shutil.move(file_path, destination)  
        print(f"Moved: {filename} → {category}/")  
    except Exception as e:  
        print(f"Error moving {filename}: {e}")

if name == "main":
target_directory = input("Enter the directory path to organize: ").strip()
organize_files(target_directory)