names = ["Adlet", "Aruzhan", "Dias"]
scores = [95, 88, 76]

print("=== enumerate() ===")
for index, name in enumerate(names, start=1):
    print(index, name)

print("=== zip() ===")
for name, score in zip(names, scores):
    print(name, score)

print("=== type checking ===")
value = "123"
print(type(value))

number = int(value)
print(number + 10)
print(type(number))

float_number = float(number)
print(float_number)
print(type(float_number))
