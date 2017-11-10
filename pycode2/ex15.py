# Reading files
"""
Usage:
     ex15.py <filename>
"""

#importing the module
from sys import argv

#unpack the content received from commandline
script, filename = argv

# open fhe file specified in cli argument
txt = open(filename)

# print the name of file
print "Here's your file %r:" % filename
#print the content of the file with read() method
print txt.read() # invoking function on file  check pydoc file

print "Type the filename again:"
# get the new filename from user
file_again = raw_input('> ')

# open the new file name received
txt_again = open(file_again)

#print the content of the new file
print txt_again.read()

"""
when <file-object>.read() is invoked on file object the position is moved to EOF
can use <file-object>.seek(position) to move the position to the specified value
to get current position use <file-object>.tell() method
use <file-object>.close() method to close the file properly
for other methods try help(file) or pydoc file
? how to ge the last position in a file no len() method here
"""