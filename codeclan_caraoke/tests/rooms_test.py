import unittest
from classes.room import *
from classes.guest import *
from classes.songs import *



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Indie Rock & World Music")
        self.song_1 = Song("Intro by The XX")
        self.song_2 = Song("Wicked Games cover by Parra for Cuva")
        
        
    
    def test_room_has_name(self):
        self.assertEqual("Indie Rock & World Music", self.room.room_name)

    def test_room_playlist__empty(self):
        self.assertEqual(0, len(self.room.playlist))
    
    def test_room_playlist__1_song(self):
        self.room.add_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room.playlist))

    def test_add_2_to_playlist__result_2(self):
        self.room.add_to_playlist(self.song_1)
        self.room.add_to_playlist(self.song_2)
        self.assertEqual(2, len(self.room.playlist))
    
    def test_add_3_to_playlist__result_2(self):
        self.room.add_to_playlist(self.song_1)
        self.room.add_to_playlist(self.song_2)
        self.room.add_to_playlist(self.song_2)
        self.assertEqual(2, len(self.room.playlist))

    
        

    
