# asking questions - here we'll take teh user input
# Note : The ',' at end of each line will stop new line after prompt
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()       # raw_input() is safe than input()

# note the %r in height will make it print the raw string - %s will print as accepted from user
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)