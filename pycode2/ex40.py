#!/usr/bin/env python2.7
"""First class example"""

class Song(object):
    '''Some imp things to Note:
    for __init__() or any other function self argument is required for initialization
    init initializes the class object so the attribute should have the 
    '''
    def __init__(self, lyrics = ["Tong tong", "Is a new Song"]):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", 
                    "I don't want to get sued",
                    "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_song = ["\nNanha muha rahi hu",
            "Desh ka sipahi Hu..."]
his_song = ["\nSare Jahan se accha",
            "Hindostan hamara..."]

song_obj1 = Song(my_song)

song_obj1.sing_me_a_song()