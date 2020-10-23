import unittest
from classes.room import *
from classes.guest import *
from classes.songs import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Indie Rock & World Music")
        
    
    def test_room_has_name(self):
        self.assertEqual("Indie Rock & World Music", self.room.room_name)

    def test_room_playlist__empty(self):
        self.assertEqual(0, len(self.room.playlist))
    
    def test_room_playlist__1_song(self):
        self.assertEqual(1, len(self.room.playlist))


    

