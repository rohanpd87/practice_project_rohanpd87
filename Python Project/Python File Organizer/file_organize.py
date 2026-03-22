import os
import shutil

down_path = input("enter the path where u want to work: ")

# Count before organizing
files = 0
folders = 0

for item in os.listdir(down_path):

    if item.startswith("."):
        continue

    full_path = os.path.join(down_path, item)

    if os.path.isfile(full_path):
        files += 1
    elif os.path.isdir(full_path):
        folders += 1

print("Before organizing:")
print("Files:", files)
print("Folders:", folders)


# Organize inside each folder
for root, dirs, down_files in os.walk(down_path):

    for file in down_files:

        if file.startswith("."):
            continue

        file_path = os.path.join(root, file)
        ext = os.path.splitext(file)[1].lower()

        # categories
        if ext in [".jpg", ".png", ".jpeg", ".webp"]:
            folder = "Images"
        elif ext in [".mp4", ".mov"]:
            folder = "Videos"
        elif ext in [".pdf", ".docx", ".pptx", ".xlsx", ".csv", ".rtf"]:
            folder = "Documents"
        elif ext in [".py", ".ipynb", ".php"]:
            folder = "Code"
        elif ext in [".exe", ".dmg", ".msi"]:
            folder = "Installers"
        elif ext in [".zip"]:
            folder = "Archives"
        elif ext in [".mp3"]:
            folder = "Audio"
        else:
            folder = "Others"

        dest_folder = os.path.join(root, folder)

        os.makedirs(dest_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(dest_folder, file))

print("Organized inside each folder")