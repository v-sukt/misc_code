#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A simple variable assignment
types_of_people = 10
x = f"There are {types_of_people} types of People."

binary = "binary"
do_not = "don't"
# String substitution for f"" - format string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

# This is another way t handle the things of formatting - i.e. using .format()
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with right side."

# This performs the addition of strings and provides the argument to the print() function
print(w + e)