import mystuff as ms  # here from mystuff import ... wont work when called from commandline
# this method of import will work if there is no __init__ in your package
from firstclass import song
# import firstclass as fs
# now access class as fs.Song()
# can also be imported as
# from firstclass.song import Song


mystuff = {'apple': "I AM APPLES!"}
print(f"From {__name__}")

# get apple from dict
# dict style
print(mystuff['apple'])

# get apple from module
# Module style
ms.apple()
print(ms.tangerine)

# class style
thing = ms.MyStuff()
thing.apple()
print(thing.tangerine)

print(f"calling happy_bday from {__name__} to sing again")
# this is at module level - no multiple objects - good for static values
# like logging.DEBUG
song.happy_bday.sing_me_a_song()

bulls_on_parade = song.Song(["They rally around tha family",
                            "With pockets full of shells"])
bulls_on_parade.sing_me_a_song()
