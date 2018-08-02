#!/usr/bin/env python2.7
"""This example is to demonstrate the inheritance - overriding the parent's function in child
for difference bahaviour"""

class Parent(object):

    def override(self):
        print "I'm in Parent's override()"

class Child(Parent):

    def override(self):
        print "I'm in child's override()"

child = Child()
parent = Parent()

parent.override()
child.override()