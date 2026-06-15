numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x > 3, numbers))
print(result)


numbers = [10, 15, 20, 25]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


names = ["Adlet", "Tom", "Alexander"]

result = list(filter(lambda x: len(x) > 4, names))
print(result)


numbers = [-2, -1, 0, 1, 2]

result = list(filter(lambda x: x > 0, numbers))
print(result)