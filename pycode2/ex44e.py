#!/usr/bin/env python2.7

""" The inheritance is good, but can be complex, there is other possibility to achieve what we did in last part 44d
This is called Composition. we can compose the object of other class and invoke it as part of child's initialization
So in other words, this way a is-a can be replaced with has-a relationships

When to use Inheritance or composition?
    Both are used when trying to solve the problem of re-usable code. 

- Inheritance solves this problem by creating a mechanism for you to have implied features in base classes. 
- Composition solves this by giving you modules and the ability to simply call functions in other classes.

Some guidelines form Zed:
1. Avoid multiple inheritance at all costs, as it's too complex to be useful reliably. If you're stuck with it, 
    then be prepared to know the class hierarchy and spend time finding where everything is coming from.
2. Use composition to package up code into modules that are used in many different unrelated places and situations.
3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept
    or if you have to because of something you're using.

So inheritance when there are like strings under same umbrella relating with one another, whereas if they are tools in some 
toolkit, composition is better"""

class Other(object):
    """Other class example for demo"""
    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "CHILD, before OTHER altered()"
        self.other.altered()
        print "CHILD, after OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()