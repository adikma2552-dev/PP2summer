from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

total = reduce(lambda x, y: x + y, numbers)
print("Sum with reduce:", total)

print("len:", len(numbers))
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sorted descending:", sorted(numbers, reverse=True))
