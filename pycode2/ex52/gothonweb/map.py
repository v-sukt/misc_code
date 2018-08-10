"""The module has following classes:
- Room"""
from random import randint

class Room(object):
    '''Takes name and description of the object and initializes paths.\nProvides methods \n\t go(direction) and,\n\t add_paths(paths)''' 

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        return self.paths.update(paths)

    def __eq__(self, room):
        if self.name == room.name and self.description == room.description and self.paths == room.paths:
            return True
        else:
            return False


central_corridor = Room("Central Corridor", 
    """The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.\n
You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you. 

What'ld you do?(shoot!/dodge!/tell a joke)""")

laser_weapon_armory = Room("Laser Weapon Armory", 
    """Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
    Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.

The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.    

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.

You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.

The Code (321)/(132)/(123)/(312)/(213)/(231):   """)

the_bridge = Room("The Bridge", 
    """The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.

What'ld you do?(throw the bomb/slowly place the bomb/something else)  """)

escape_pod = Room("Escape Pod", 
    """You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.

You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.

Now that the bomb is placed you run to the escape pod to
get off this tin can. 

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?   (1)(2)(3)(4)(5)""")

the_end_winner = Room("The End", 
    """You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  

Your fedback about the game! : """)

the_end_looser = Room("The End", 
    """You jump into random pod and hit the eject button
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.""")

quips = [ "You dead. You kinda suck a this.", 
        "Your mom would be proud...if she were smarter",
        "Such a luser.",
        "I've a small puppy that's better at this."
        ]

generic_death = Room("Death", "You died."+quips[randint(0, len(quips)-1)])

escape_pod.add_paths({
        '2': the_end_winner,
        '*': the_end_looser
    })

the_bridge.add_paths({
        'throw the bomb': generic_death,
        'slowly place the bomb':escape_pod
    })

laser_weapon_armory.add_paths({
        '123': the_bridge,
        '*': generic_death
    })

central_corridor.add_paths({
        'shoot!': generic_death,
        'dodge!': generic_death,
        'tell a joke': laser_weapon_armory,
        '*': generic_death
    })

START = central_corridor

#class Map(object):
#
#    scenes = {
#        'central_corridor' : CentralCorridor(),
#        'laser_weapon_armory' : LaserWeaponArmory(),
#        'the_bridge' : TheBridge(),
#        'escape_pod' : EscapePod(),
#        'death' : Death()
#    }
#
#    def __init__(self, start_scene):
#        self.start_scene = start_scene
#
#    def next_scene(self, scene_name):
#        return Map.scenes.get(scene_name)
#
#    def opening_scene(self):
#        return self.next_scene(self.start_scene)
#
#
#a_map = Map("central_corridor")
#a_game = Engine(a_map)
#a_game.play()#