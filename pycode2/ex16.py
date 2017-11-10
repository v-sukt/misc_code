"""exercise about reading and writing into the files
Usage:
     ex16.py <filename>
important methods to remember:
close - close the file saving the content
read - red entire file, assign the content to variable
readline - read one line from the file
truncate - remove the contents of file - be careful with this
write(stuff) - write stuff in the file
"""
from sys import argv

script, filename = argv

print "We are going to erase the content of %r" % filename
print "If you don't want this, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?') # just get the input, but do nothing - used as pause

print "Opening the file..."
target = open(filename, 'w') # read file in write mode

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)  # note- the escape sequence won't work - its raw input
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()