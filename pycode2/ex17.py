#!/usr/bin/env python2.7
"""
Some more work on files - copy code from one file to another
new module : os
removing the ## - double comments is another way of making it short
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s file to %s file" % (from_file, to_file)

# we could do this on one line too, how?
##in_file = open(from_file)  #can bw written with ';' separator between lines
##indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long." % len(indata)

print "Does the target exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("?")

# if the mode 'w'/'a' is not specified you can't write to file
# if used the file is created if doesn't exist
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
##in_file.close() # Not required if in_file is not defined. file's closed by python
