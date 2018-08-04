#!/usr/bin/env python2.7
""" Some space for my own gam.
Some guidelines form Zed
 - use camecase for class names
 - use exact names for the functions(to indicate what they do) but not big name - you'll have to tyype that long name multuple times
    * like list.pop() not list._remove_the_last_element_from_ist()
 - keep the sequence of arguments same for functions of same class - if they take similar arguments | easy for using/remembering the order
 - Try not to do too much in __init__ functions, that makes them harder to use
 - Give enogh vertical space in your code - makes it more readable
 - If you can't read it loud it's probably hard to read. If you are having a problem making something easy to use, 
   try reading it out loud. Not only does this force you to slow down and really read it, but it also helps you 
   find difficult passages and things to change for readability.
 - Write good comments for function, as some other person is gonna use it - may be you will forgot what you did and 
   why/how you did it
 - When you write doc comments for your functions, make the comments documentation for someone who will have to use 
   your code. You do not have to go crazy, but a nice little sentence about what someone can do with that function helps a lot.

Something about the Game:
 * taking some scnario from harry potter series 
   - Ron's chess
   - Duet of magic with Malfoy
   - Escape from the Dragon in the First Task of Trivizard Tournament **
   - Interact with Hagrid's brother + the scene when they are caught while tresspassing the office of Dolores Umbridge
"""

import ex45_src.mapengine as mape

a_map = mape.Map('hogwards_dormitory')
a_game = mape.Engine(a_map)
a_game.play()