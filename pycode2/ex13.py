#!/usr/bin/env python2.7
# Taking parameters from commandline

# This line is to add feature to script from Python feature set
from sys import argv # importing a module

# Unpack the argv contents into the four variables
script, first, second, third = argv
# You'll get an error if no arguments are provided

# Get more details by prompting
fourth = raw_input("Any additional arguments? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Additional argument is:", fourth # works even if no input provided
