from datetime import datetime

now = datetime.now()

print("Current date and time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

formatted = now.strftime("%d/%m/%Y")
print("Formatted date:", formatted)

birthday = datetime(2007, 3, 29)

difference = now - birthday

print("Days since birthday:", difference.days)