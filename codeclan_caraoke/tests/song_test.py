import unittest
from classes.songs import *

class TestSongs(unittest.TestCase):

    def setUp(self):
        # self.song = Song()
        self.song = Song("Smash by The Offspring")
        self.song_0 = Song("Test1")
        self.song_1 = Song("Test2")
        self.song_2 = Song("Youth Edit by Markus Toepfer")
        self.song_3 = Song("Come as you are by Nirvana")
        
    def test_add_song_to_library(self):
        self.song.add_to_song_library(self.song_2)
        self.assertEqual(1, len(self.song.song_library))
    
    def test_remove_song_to_library(self):
        self.song.add_to_song_library(self.song_2)
        self.song.remove_song_library(self.song_2)
        self.assertEqual(0, len(self.song.song_library))

    # def test_display_library__result_empty(self):
    #     self.song.print_library()
    #     self.assertEqual([], self.song.song_library)

    # def test_display_library__result_2(self):
    #     self.song.add_to_song_library(self.song_0)
    #     self.song.add_to_song_library(self.song_1)
    #     self.song.print_library()
    #     self.assertEqual(["Test1", "Test2"], self.song.song_library)