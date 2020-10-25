import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 20, "A Candle's Fire by Beirut")
    
    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest.wallet)
    
    def test_guest_has_fav_song(self):
        self.assertEqual("A Candle's Fire by Beirut", self.guest.fav_song)

    def test_guest_list(self):
        self.assertEqual(0, len(self.guest.guest_list))

    def test_add_to_guest_list(self):
        self.guest.add_to_guestlist(Guest)
        self.assertEqual(1, len(self.guest.guest_list))

    def test_remove_guest_from_list(self):
        self.guest.add_to_guestlist(Guest)
        self.guest.remove_guest_from_list(Guest)
        self.assertEqual(0, len(self.guest.guest_list))