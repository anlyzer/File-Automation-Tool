import os
import shutil
from datetime import datetime

# Folder to organize
SOURCE_FOLDER = "test_folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".docx"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

LOG_FILE = "log.txt"

# Write log function
def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# Main function
def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("❌ Folder not found!")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    write_log(f"Moved {file} to {folder}")
                    moved = True
                    break

            if not moved:
                target_folder = os.path.join(SOURCE_FOLDER, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                write_log(f"Moved {file} to Others")

    print("✅ Files organized successfully!")

# Run program
organize_files()
