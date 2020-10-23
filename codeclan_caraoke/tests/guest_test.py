import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ian", 20, "A Candle's Fire by Beirut")
    
    def test_guest_has_name(self):
        self.assertEqual("Ian", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest.wallet)
    
    def test_guest_has_fav_song(self):
        self.assertEqual("A Candle's Fire by Beirut", self.guest.fav_song)