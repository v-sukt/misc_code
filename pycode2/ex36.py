#!/usr/bin/env python2.7

def if_guide():
    print "*"*20, """\nIf Guide:\n
    - every if statement must have else
    - if this else should neve be run because it doesn't make sense, the U must use die function in else -- will help find many errors!!
    - never nest if statements more than two deep and always try to do them one deep, if not possible move innner if if another function
    - treat if staments like paragraphs, where each if, elif, else grouping is like set of sentences 
        * put blank lines before and after 
    - make boolean tests simple to understand (more readable), else move the calculations earlier in readable variable

    ! break the rules if necessary but follow Xen of python, don't follow rules just for sake of following them. Doesn't always make sense 
     """

def loop_guide():
    print "*"*20, """\nLoop Guide:\n
    - use while only to loop forever and that means probably never. (only for python)
    - use for loop for looping, especially if there is a fixed or number of things to loop over!!
    """

def debug_guide():
    print "*"*20, """\nDebug Guide\n
    - Don't use debugger, its like full body-scan on a sick person.. quite confusing
    - better way is to use print statements to know what's value of the variables
    - make sure parts of program work as you work on them, In other words don't start testing after it's already few files. Code - run - fix - code
    ! Code a little, run a little, fix a little
    """

if __name__ == "__main__":
    #print all only if executed as main module
    if_guide()
    loop_guide()
    debug_guide()
else:
    print "imported functions : \nif_guide()\nloop_guide()\ndebug_guide()\n"

