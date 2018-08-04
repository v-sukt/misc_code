#!/usr/bin/env python2.7
"""This example is to demonstrate the inheritance - demonstrate all 3 ways:
    * calling parent's inherited version
    * calling overriden version
    * calling parent's version from overridden function
why super()?
    when a child class is inherited from multi-parents (Multiple-Inheritance) to look up the functions from parents 
Python uses mro (Method resolution order) and C3 algorithm. So when you try to call multi-parent's function from same class... 
It's just unpredictable - here in following example it only invokes the method from first class in the list
    Though Otherwise the super() works well for initializing the parent like in __init__() of the child"""

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"

class BadStuff(object):

    def altered(self):
        print "BadStuff's altered()"

class TeenChild(BadStuff, Parent):

    def altered(self):
        print "Before calling super()"
        super(TeenChild, self).altered()
        print "After calling super()"


dad = Parent()
son = Child()

# Implicit function
print "-"*20
dad.implicit()
son.implicit()

# Override functions
print "-"*20
dad.override()
son.override()

# Altered functions
print "-"*20
dad.altered()
son.altered()

# For multi-inheritance example
print "-"*20
teen = TeenChild()
teen.altered()