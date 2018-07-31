#!/usr/bin/env python2.7
''' Example demonstrating few functions of list and string
The python functions used
    str.join(separator, list) -> str : join the list elements with specified separator and return a string
    str.split(seperator, list) -> list : split the string based on the specified separator
    list.append(list, object-to-append) -> list : append new elements at the end of the string
    list.pop(index) -> element : removes teh object at index(default last) from the list
    len(list) -> int : number of elements in list
'''

ten_things = "Apples Pranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let'x fix that."
#created a list splitting the string with separator ' '
stuff = ten_things.split(' ') 
#another referece list to get elements from
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] 

while len(stuff) != 10: #condition till the no. of elements to be 10
    next_one = more_stuff.pop()  #remove last elemnent and assign to var
    print "Adding: ", next_one   
    stuff.append(next_one)       #append the element from var to list
    print "There's %d items now." % len(stuff)

#print the final list
print "There we go: ", stuff

print "Let's do some thigs with stuff"

print stuff[1] #element at 1/second element
print stuff[-1] #last element
print stuff.pop()
print ' '.join(stuff) #single string with all elements separated with ' '
print '#'.join(stuff[3:5]) #join from element 'at 3' to 'fifth' element
