class Song(object):

  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line

happy_birthday = Song(["""
Happy birthday to you
I don't want to get sude
So I'll stop right here.
"""])

bulls_on_parade = Song(["""
They rally 'round yo' family
With a pocket full of shells
"""])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()