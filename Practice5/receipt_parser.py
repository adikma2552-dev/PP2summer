import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("=== SEARCH ===")
result = re.search(r"ИТОГО", text)

if result:
    print("Word found!")

print("\n=== FINDALL ===")
prices = re.findall(r"\d+,\d{2}", text)
print(prices[:10])

print("\n=== SPLIT ===")
words = re.split(r"\s+", text)
print(words[:10])

print("\n=== SUB ===")
clean_text = re.sub(r"\s+", " ", text)
print(clean_text[:100])

print("\n=== DATE ===")
date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)

if date:
    print(date.group())

print("\n=== PHONE ===")
phone = re.search(r"\+7\d+", text)

if phone:
    print(phone.group())