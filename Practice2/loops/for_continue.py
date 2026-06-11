for i in range(1, 6):
    if i == 3:
        continue
    print(i)


for letter in "Python":
    if letter == "h":
        continue
    print(letter)


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)