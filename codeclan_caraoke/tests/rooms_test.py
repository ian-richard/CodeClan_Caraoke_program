import unittest
from classes.room import *
from classes.guest import *
from classes.songs import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Indie Rock & World Music")
        self.song_1 = Song("Intro by The XX")
        self.song_2 = Song("Wicked Games cover by Parra for Cuva")
        self.guest = Guest("Ian", 20, "A Candle's Fire by Beirut")
        self.guest_2 = Guest("Ann", 20, "Song2")
        self.guest_3 = Guest("Carly", 20, "Song3")
        self.guest_4 = Guest("Jane", 20, "Song4")
        self.guest_5 = Guest("James", 20, "Song5")
        self.guest_6 = Guest("Hannah", 20, "Song6")
        self.guest_7 = Guest("Andy", 20, "Song7")
        self.guest_skint = Guest("Flint", 0, "Song_8")
    
    def test_room_has_name(self):
        self.assertEqual("Indie Rock & World Music", self.room_1.room_name)

    def test_room_playlist__empty(self):
        self.assertEqual(0, len(self.room_1.playlist))
    
    def test_room_playlist__1_song(self):
        self.room_1.add_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_add_2_to_playlist__result_2(self):
        self.room_1.add_to_playlist(self.song_1)
        self.room_1.add_to_playlist(self.song_2)
        self.assertEqual(2, len(self.room_1.playlist))
    
    def test_remove_track_playlist__result_0(self):
        self.room_1.add_to_playlist(self.song_1)
        self.room_1.remove_track_playlist(self.song_1)
        self.assertEqual(0, len(self.room_1.playlist))
    
    def test_get_capacity_of_room(self):
        self.assertEqual(6, self.room_1.get_capacity())

    def test_add_guest_to_room__success(self):
        self.room_1.add_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room_1.guests))
    
    def test_add_guest_to_room__failure__no_money(self):
        self.room_1.add_guest_to_room(self.guest_skint)
        self.assertEqual(0, len(self.room_1.guests))
    
    def test_remove_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest)
        self.room_1.add_guest_to_room(self.guest)
        self.room_1.remove_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room_1.guests))
        

    def test_add_guest_room_full(self):
        self.room_1.add_guest_to_room(self.guest)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.add_guest_to_room(self.guest_4)
        self.room_1.add_guest_to_room(self.guest_5)
        self.room_1.add_guest_to_room(self.guest_6)
        self.room_1.add_guest_to_room(self.guest_7)
        result = self.room_1.free_spaces()
        result_2 = self.room_1.number_of_guests_in_room()
        self.assertEqual(None, result)
        self.assertEqual(6, result_2)
        
    
    def test_room_has_free_space(self):
        self.room_1.add_guest_to_room(self.guest)
        result = self.room_1.free_spaces()
        self.assertTrue(5, result)

    def test_room_till_empty(self):
        self.assertEqual(0, self.room_1._till)


        

    

