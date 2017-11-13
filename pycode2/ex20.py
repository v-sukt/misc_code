'''
Using functions and files

Usage:
      script-name <input-file>
'''
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    # seek's argument is in bytes not number of lines
    f.seek(0)

def print_a_line(line_count, f):
    # the print function prints a line ending with '\n' <-- from the file
    # and adds own '\n' that comes at end of print.
    print line_count, f.readline(), # adding ',' avoids extra '\n' in output
    # with ',' the newline appearing is from the file's contents

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1

print_a_line(current_line, current_file)

current_line += 1 #Augmented increment eqvt. of current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)