#!/usr/bin/env python2.7

""" Guidelines for Object Oriented Analysis and Design:
1. Write down about the problem
2. Extract Key cnocepts from #1 and reseach them
3. Create a class hierarchy and object map for the concepts - in object has-a is-a fastion 
4. Code the classes and a test to run them
5. Repeat and refine iti
It's all like form a very abstract idea and then solidify it further.
Now draw some diagrams depicting the relationship between various things and write description of these things. 
  - once it's perfect (covers all things needed) separate the nouns and verbs from it (classes/objects and methods).
  - ensure that you fully understand it and can visualize it, if not do some research on them and undestand
  - get some rough common relations between nouns and how others can be related to each other || a basic hierarchy for classes
  - check which of these names are similar things? 
    * like same thing - for class and instance of it "
    * What is basically just another word for another thing?"
  - create a basic structure and some code - test that it works
  - keep on adding some code and testing it's working, repeat and refine

    The mehod used earlier is called top-down method where at top it's just abstract and towards bottom gets more solofied. 
There is another way which one can use as one become good at programming and there is some part of this bug puzzle known to you
and can think the problem in terms of code. Some steps for this way (Bottom Up):
1. Take a small piece of the problem; hack on some code and get it to run barely.
2. Refine the code into something more formal with classes and automated tests.
3. Extract the key concepts you're using and try to find research for them.
4. Write up a description of what's really going on.
5. Go back and refine the code, possibly throwing it out and starting over.
6. Repeat, moving on to some other piece of the problem.
Remember that your solution will probably be meandering and weird, so that's why Zed's version of this process involves going 
back and finding research then cleaning things up based on what you've learned.
"""

from sys import exit
from random import randint

class Scene(object):
        
    def enter(self):
        print "This scene is not yet cofigured. Subclass it and implement enter()"
        exit(1)


class Engine(object):
     
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    quips = [ "You doed. You kinda such a this.", 
        "Your mom would be proud...if she were smarter",
        "Such a luser.",
        "I've a small puppy that's better at this."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(sef):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map("central corridor")
a_game = Engine(a_map)
a_game.play()


