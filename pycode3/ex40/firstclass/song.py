class Song(object):
    """My first sample class"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])
# called once at the time of first import - so comes at module level not at class level
happy_bday.sing_me_a_song()
