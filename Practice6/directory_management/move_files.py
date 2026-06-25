from pathlib import Path
import shutil

source_folder = Path("source")
destination_folder = Path("destination")

source_folder.mkdir(exist_ok=True)
destination_folder.mkdir(exist_ok=True)

source_file = source_folder / "example.txt"
source_file.write_text("This file will be moved and copied.", encoding="utf-8")

copied_file = destination_folder / "copied_example.txt"
shutil.copy(source_file, copied_file)
print("File copied to destination folder.")

moved_file = destination_folder / "moved_example.txt"
shutil.move(source_file, moved_file)
print("File moved to destination folder.")

print("Destination folder files:")
for file in destination_folder.iterdir():
    print(file.name)
