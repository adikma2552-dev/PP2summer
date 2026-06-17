# Iterator

numbers = [1, 2, 3]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


# Generator

def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for i in count_up_to(5):
    print(i)


# Generator expression

squares = (x * x for x in range(5))

for square in squares:
    print(square)