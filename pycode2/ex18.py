"""
functions creation. some sample functions
each will start with def keyword, function name followed by ':'
then contents indented
"""
# this one is like your scripts with argv
# arguments are taken and kept in args as list
def print_two(*args): #this is much like argv for script
    arg1, arg2 = args
    print "arg1: %r, arv2: %r" % (arg1, arg2)

# OK, that *args is pointless we'll just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no argument
def print_none():
    print "I got nothin."


print_two("v","sukt")
print_two_again("v","sukt")
print_one("First!")
print_none()