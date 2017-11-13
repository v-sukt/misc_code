'''
Functions returning values and use of function's return value as direct argument
'''

# some functions returning some value
def add(a, b):
    print "Adding %r and %r" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %r from %r" % (b, a)
    return a - b

def multiply(a, b):
    print "Multiplying %r and %r" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %r by %r" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78.0, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

# Calling a function from inside of another function
# The innermost is evaluated first then the external one
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"