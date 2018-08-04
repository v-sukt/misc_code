"""This file contains all the scenes from the ex45 sample game"""

from sys import exit
from random import sample

class Scenes(object):
    
    def enter_scene(self):
        print "This is not written, override the function"


class WalkInForbiddenForest(Scenes):
    
    def enter_scene(self):
        return 'lost_path'


class TalkGwarp(Scenes):

    def enter_scene(self):
        return 'horsemen'


class LostPath(Scenes):
    
    def enter_scene(self):
        return 'talk_gwarp'


class HorseMen(Scenes):
    """docstring for HorseMen"""
    
    def enter_scene(self):
        return 'finish'


class HogartsDormitory(Scenes):
    """Scene where harry get dream and tell Harmione and Ron"""
    
    def enter_scene(self):
        return 'dolores_office'


class DoloresOffice(Scenes):

    def enter_scene(self):
        return 'walk_in_forest'


class Finish(Scenes):

    def enter_scene(self):
        coupon = sample("ZxCvBnM0123456789QaWsEdRfTgYhUjIkOl", 10)
        print """\tCongratulations...
        You have successfully managed getting rid of that Dolores Bitch (literally) 
        ...and restoring the former glory of Hogwarts School of Witchcraft and Magic!!
        Use following Coupon for Wisley's Shop for getting gifts worthy of 3 golden Galleons : 
        \n\t\t%s\n\n""" % "".join(coupon)

        exit(0)

class GameOver(Scenes):

    def enter_scene(self):
        exit(1)