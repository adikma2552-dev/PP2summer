from pathlib import Path

file_path = Path("sample.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python file handling\n")
    file.write("This file was created with write mode.\n")
    file.write("Practice 6 example\n")

print("File created and data written successfully.")
