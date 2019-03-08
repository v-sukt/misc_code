"""Something on user input"""
print("How old are you?", end=' ')  # end is provided so it won't use newline (by default)
age = input()
print("How tall are you?", end=' ')
height = input()
weight = input("How much do you weigh? ")  # this is another way - can directly prompt in input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
