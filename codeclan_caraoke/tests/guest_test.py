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

    def test_guest_can_afford_entry(self):
        result = self.guest.can_afford_entry(5)
        self.assertEqual(True, result)

    def test_deduct_fee_from_wallet(self):
        result = self.guest.deduct_fee(5)
        self.assertEqual(15, self.guest.wallet)
        
        