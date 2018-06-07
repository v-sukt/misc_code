# Here we can write the values directly on right of %
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Example of using multiple variables and printing in a string
y = "There who know %s and those who %s" % (binary, do_not)

print x
print y

# the string with formatter printed as raw string with %r
print "I said: %r" % x
# The string with multiple string substitution as %s in single quote
print "I also said: '%s'" % y

# Create the binary variable
hilarious = False
# Create a string with formatter (raw - %r)
joke_evaulation = "Isn't that joke so funny?! %r"

#Print the binary variable with %r formatter inside a string - gives value of it
print joke_evaulation % hilarious

# create a string parts to be printed later as combine string
w = "This is the left side of..."
e = "a string with right side."

# we can even print the combination of strings with + operator
print w + e