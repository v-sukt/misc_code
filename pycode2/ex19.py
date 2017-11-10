"""
Some examples of variables as arguments to function
"""
# This function takes arguments and prints
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enoguh for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # providing the numbers as arguments


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# provide the variables to pass values
cheese_and_crackers(amount_of_cheese, amount_of_crackers) 

print "We can even do math inside too:"
# add the numbers while providing the argument
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
# Do some small math while providing the argument to function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
