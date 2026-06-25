from pathlib import Path

file_path = Path("sample.txt")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("New line was appended to the file.\n")
    file.write("Append mode does not delete old data.\n")

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
