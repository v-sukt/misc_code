# import mystuff as ms - Doesn't work for import module
from .mystuff import tangerine, apple, MyStuff
from .firstclass.song import Song, happy_bday

mystuff = {'apple': "I AM APPLES!"}
print(f"From {__name__}")

# get apple from dict
# dict style
print(mystuff['apple'])

# get apple from module
# Module style
apple()
print(tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

print(f"calling happy_bday from {__name__} to sing again")
happy_bday.sing_me_a_song()

bulls_on_parade = Song(["They rally around tha family",
                       "With pockets full of shells"])
bulls_on_parade.sing_me_a_song()
