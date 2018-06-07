# Here's some new strange stuff, remember to type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
# String with new-line character - '\n'
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Output the string values from above
print "Here are the days: ", days
# the newline is printed if %s is used but will remain as is with %r
# Note: %r for debugging and %s is for displaying
print "Here are the months: ", months

# The multiline string enclosed within ''' or """
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Event 4 lines if we want, or 5, or 6.
"""
# This style is also used to add the help section