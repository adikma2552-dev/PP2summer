from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists():
    print("=== read() ===")
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())

    print("=== readline() ===")
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.readline())

    print("=== readlines() ===")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
else:
    print("File does not exist. Run write_files.py first.")
