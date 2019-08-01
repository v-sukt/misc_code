from .mycode import Map, Engine
__doc__="""
A small game to help understand the designing based on OOP concepts. 
Defined various scenes each with enter() which returns the next scene key.
    - CentralCorridor
    - LaserWeaponArmory
    - TheBridge
    - EscapePod
    - Death
    - Finished
Map is defined with keys, Scene subclass objects as dict and with method 
    - to provide first object and 
    - to provide object based on the key provided
Engined is defined with constructor of Map object and method play to iterate over the scenes till game reaches 
    Finished() object
    
To use just import the Package and run something like
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
    
"""
