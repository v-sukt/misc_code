#!/usr/bin/env python3.6

my_name = 'v-sukt'
my_age = 45 # :)
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

# NOTE: following format method will only work on python3.6 will give error with python3.4
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}. {my_height} and {my_weight} I get {total}.")