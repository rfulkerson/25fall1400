name = "Robert"
print("Hello there")

print(len(name))

print(name[0])
print(name[len(name) - 1])

print("Hello" + " " + "there, " + name)
print("Hello", "there", name)
print("Ho" * 3)

print(f"Hello there, {name}, how are you?")

print(f"Hello there, {name:s}, how are you?")

pi = 3.14159

print(f'The value of pi is {pi:f}')
print(f'The value of pi is {pi:.2f}')

age = int(input("Enter age: "))  # explicit conversion

result = 5 * 2.5  # implicit conversion

print(result)

weird_math = 7 * int(pi)  # explicit conversion

print(weird_math)

