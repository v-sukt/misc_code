"""reading from a file"""

from sys import argv
try:
    script, filename = argv
except Exception as e:
    print("Operation failed", e)
    exit(1)

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again :")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
