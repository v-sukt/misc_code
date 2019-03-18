"""Else-If statements"""
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# check if cars are more than people and if trucks are less than cars
if cars > people and trucks < cars:
    print("We should take the cars.")
    print("Maybe we could take the trucks.")
# check of cars are less than people and trucks are more than cars
elif cars < people and trucks > cars:
    print("We should not take the cars.")
    print("That's too many trucks.")
# if neither is case
else:
    print("We can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
