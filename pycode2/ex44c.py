#!/usr/bin/env python2.7
"""This example is to demonstrate the inheritance - using parent's behaviour After/before changed child's behaviour
Internally calls tha parent function uspng super()"""

class Parent(object):

    def altered(self):
        print "Parent's altered()"

class Child(Parent):

    def altered(self):
        print "\nChild, before Parent altered()"
        super(Child, self).altered()
        print "Child, after Parent altered()"

child = Child()
parent = Parent()

parent.altered()
child.altered()