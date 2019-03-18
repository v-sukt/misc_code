ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("elements: ",ten_things, "\nWait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

# prints the element at 1
print(stuff[1])
# print element 1st element from end
print(stuff[-1])
# remove an element
print(stuff.pop())
# join the elements of list with space
print(' '.join(stuff))
# join the elements of list with '#'
print('#'.join(stuff))
