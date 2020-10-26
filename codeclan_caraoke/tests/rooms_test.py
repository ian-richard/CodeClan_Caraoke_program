import unittest
from classes.room import *
from classes.guest import *
from classes.songs import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Indie Rock & World Music")
        self.song_1 = Song("Intro by The XX")
        self.song_2 = Song("Wicked Games cover by Parra for Cuva")
        self.guest = Guest("Ian", 20, "A Candle's Fire by Beirut")
    
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
    
    def test_remove_track_playlist__result_0(self):
        self.room.add_to_playlist(self.song_1)
        self.room.remove_track_playlist(self.song_1)
        self.assertEqual(0, len(self.room.playlist))

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room.guests))
    
    def test_remove_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.remove_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_add_guest_room_full(self):
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.assertEqual(6, len(self.room.guests))
        self.assertEqual("Room Full", self.room.add_guest_to_room)

    # def test_max_room__has_capacity__True(self):
    #     self.room.add_guest_to_room(self.guest)
    #     self.assertEqual(1, len(self.room.guests))
    
    def test_room_guests_list_less_than_capacity(self):
        self.assertTrue(self.room.capacity)
        

    

