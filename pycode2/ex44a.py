#!/usr/bin/env python2.7
"""This example is to demonstrate the inheritance - calling parent functin from child"""

class Parent(object):

    def implicit(self):
        print "I'm in Parent implicit()"

class Child(Parent):
    pass

child = Child()
parent = Parent()

parent.implicit()
child.implicit()    # This one actually calls the inherited parent's implicit function