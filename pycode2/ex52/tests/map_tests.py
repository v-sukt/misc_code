'''Here tests are run so all functions that start with test_ are executed. 
nose.tools.assert_equal() method, checks if both arguments passed to it are same'''

from nose.tools import *
from gothonweb.map import *

def test_room():
    '''Basic Test to check the basic attributes of the object'''
    gold = Room("GoldRoom", '''This room has gold in it that you can grab. There's door to the North''')
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    '''Tests to check the setting paths and retur values of the objects'''
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    '''The tests to test the tntire map'''
    start = Room("Start", "You can go west and down a hole")
    west = Room("West", "There are trees here, you can go east")
    down = Room("Dungeon", "It's dark down here, you can go up")

    start.add_paths({'west': west, 'down': down })
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('down').go('up'), start)
    assert_equal(start.go('west').go('east'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), generic_death )
    assert_equal(START.go('dodge!'), generic_death )
    
    room = START.go('tell a joke')

    assert_equal(room, laser_weapon_armory)