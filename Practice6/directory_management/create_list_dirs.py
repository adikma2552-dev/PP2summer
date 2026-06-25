from pathlib import Path
import os

base_folder = Path("test_folder")
nested_folder = base_folder / "documents" / "python"

nested_folder.mkdir(parents=True, exist_ok=True)

file1 = nested_folder / "notes.txt"
file2 = nested_folder / "data.csv"
file3 = nested_folder / "main.py"

file1.write_text("Text file example", encoding="utf-8")
file2.write_text("name,score\nAdlet,100", encoding="utf-8")
file3.write_text("print('Hello')", encoding="utf-8")

print("Current working directory:", os.getcwd())
print("Files and folders inside nested folder:")

for item in os.listdir(nested_folder):
    print(item)

print("Python files:")
for file in nested_folder.glob("*.py"):
    print(file.name)
