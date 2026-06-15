numbers = [5, 2, 8, 1]

result = sorted(numbers)
print(result)


names = ["Alexander", "Tom", "Bob"]

result = sorted(names, key=lambda x: len(x))
print(result)


students = [("Adlet", 19), ("Tom", 18), ("Alex", 21)]

result = sorted(students, key=lambda x: x[1])
print(result)


words = ["banana", "apple", "orange"]

result = sorted(words)
print(result)