import re
import json

# Read receipt text from raw.txt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Clean text: replace many spaces/new lines with one space
clean_text = re.sub(r"\s+", " ", text)

print("=== REGEX FUNCTIONS ===")

# re.search() - finds first match
search_result = re.search(r"ИТОГО", text)
if search_result:
    print("search(): word ИТОГО found")

# re.findall() - finds all matches
all_prices = re.findall(r"\d[\d\s]*,\d{2}", text)
print("findall(): first 10 prices:", all_prices[:10])

# re.split() - splits text by spaces
words = re.split(r"\s+", text)
print("split(): first 10 words:", words[:10])

# re.sub() - replaces many spaces with one space
print("sub(): cleaned text:", clean_text[:100])

# re.match() - checks beginning of text
match_result = re.match(r"ДУБЛИКАТ", text)
print("match(): starts with ДУБЛИКАТ:", bool(match_result))


print("\n=== RECEIPT PARSER ===")

# 1. Extract all prices
prices = re.findall(r"\d[\d\s]*,\d{2}", text)

# 2. Find all product names
product_names = re.findall(
    r"\d+\.\s*\n\s*(.*?)\s*\n\s*\d,\d{3}\s*x\s*[\d\s]+,\d{2}",
    text
)

# 3. Calculate / extract total amount
total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)
total_amount = total_match.group(1) if total_match else None

# 4. Extract date and time information
date_time_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})",
    text
)

date = date_time_match.group(1) if date_time_match else None
time = date_time_match.group(2) if date_time_match else None

# 5. Find payment method
payment_match = re.search(
    r"(Банковская карта|Наличные):\s*([\d\s]+,\d{2})",
    text
)

payment_method = payment_match.group(1) if payment_match else None
payment_amount = payment_match.group(2) if payment_match else None

# 6. Create structured output
receipt_data = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "payment_amount": payment_amount,
    "total_amount": total_amount,
    "product_names": product_names,
    "prices": prices
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))