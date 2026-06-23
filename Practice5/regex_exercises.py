import re

# 1
text = "abbb"
print(bool(re.fullmatch(r"ab*", text)))

# 2
text = "abbb"
print(bool(re.fullmatch(r"ab{2,3}", text)))

# 3
text = "hello_world test_string"
print(re.findall(r"[a-z]+_[a-z]+", text))

# 4
text = "Hello World Python"
print(re.findall(r"[A-Z][a-z]+", text))

# 5
text = "a12345b"
print(bool(re.fullmatch(r"a.*b", text)))

# 6
text = "Hello, world. Python regex"
print(re.sub(r"[ ,.]", ":", text))

# 7 Snake Case → Camel Case
def snake_to_camel(text):
    words = text.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world_python"))

# 8 Split at uppercase letters
text = "HelloWorldPython"
print(re.findall(r"[A-Z][a-z]*", text))

# 9 Insert spaces before capital letters
text = "HelloWorldPython"
print(re.sub(r"([A-Z])", r" \1", text).strip())

# 10 Camel Case → Snake Case
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")

print(camel_to_snake("HelloWorldPython"))