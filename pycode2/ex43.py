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

    quips = [ "You dead. You kinda suck a this.", 
        "Your mom would be proud...if she were smarter",
        "Such a luser.",
        "I've a small puppy that's better at this."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod.\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("(shoot!/dodge!/tell a joke)> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(sef):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        try:   # cheat code - just type two nos rather than one
            guess = int(raw_input("[keypad]> "))
            guesses = 0

            while guess != code and guesses < 10:
                print "BZZZZEDDD!"
                guesses += 1
                guess = int(raw_input("[keypad]> ")) # The bug in the game - there is no escape unless you compare integer with integer
        except ValueError:
            guess = code

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge' 
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'
            exit(0)


class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("(throw the bomb/slowly place the bomb/something else)> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        try:  # cheat code - just type two nos rather than one
            guess = int(raw_input("[pod #]> ")) # The bug in the game - there is no escape unless you compare integer with integer
        except:
            guess = good_pod

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button" % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"
            return 'finished'



class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()