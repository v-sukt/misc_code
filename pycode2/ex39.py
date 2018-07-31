#!/usr/bin/env python2.7
"""
For iterating dictionary use - 
    for key,value in dict.items():
  this provides tuple with key-value and gets auto-iterated - the methos is indicated at the end
dict.get(key, default_value) : provides the value corresponding to the key else returns None(default) or the indicated default value
dict.keys() and dict.values() : returns the list of keys and valuesrespectively 
Using for loop on dictionary objects:
- first it generates the iterable object 
- iterable_object.next() gives the key in return || by calling next function of the class
- on end next() raises StopIteration exception 
- if handled with try..except block can print the content
consider the following states dictionary 
try:
    nn=iter(states)
    while nn:
        key = nn.next()
        print "key- %r, value-%r" %(key, states[key])
except:
    pass
For lists iteration
state_names = states.keys()
try:
    nn=iter(state_names)
    while nn:
        value = nn.next()
except:
    pass

Check collections.OrderedDict structure
"""
# create a set with mapping of state to abbreviation
states = {
    'Maharashtra' : 'MH',
    'Orissa' : 'OR',
    'Gujarat' : 'GJ',
    'Tamilnadu': 'TN',
    'Madhyapradesh': 'MP'
}

# create a basic set of states and some cities in them
cities = {
    'MH' : 'Aamchi Mumbai',
    'GJ' : 'Badoda',
    'MP' : 'Ujjain'
}

# add some more cities
cities['OR'] = 'Jagannath Puri'
cities['TN'] = 'Mysore'

# print out some cities
print '-' * 20
print 'MH state has: ', cities['MH']
print 'GJ state has: ', cities['GJ']

# print some states
print '-' * 20
print 'Orissa\'s abbreviation is: ', states['Orissa']
print 'Tamilnadu\'s abbreviation is: ', states['Tamilnadu']

# do it by using the state then cities dict
print '-' * 20
print "Madhyapradesh has: ", cities[states["Madhyapradesh"]]
print "Orissa has: ", cities[states["Orissa"]]

# now every state abbreviation
print '-' * 20
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# now every city in state
print '-' * 20
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 20
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 20
# safely get an abbreaviation by state that might not be there
state = states.get('Goa', None)

if not state:
    print "Sorry, No Goa."

# get a city with a default value
city = cities.get('JK', 'Does Not Exist')
print "The city for the state 'JK' %s" % city
