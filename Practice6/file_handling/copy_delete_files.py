from pathlib import Path
import shutil

original_file = Path("sample.txt")
backup_file = Path("sample_backup.txt")

if not original_file.exists():
    with open(original_file, "w", encoding="utf-8") as file:
        file.write("This is sample data for backup.\n")

shutil.copy(original_file, backup_file)
print("File copied successfully.")

if backup_file.exists():
    backup_file.unlink()
    print("Backup file deleted safely.")
else:
    print("Backup file was not found.")
