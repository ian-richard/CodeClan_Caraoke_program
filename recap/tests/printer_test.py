import unittest
from classes.printer import *
# import printer 

class TestPrinter(unittest.TestCase):

    def setUp(self):
        self.printer = Printer()
    
    def test_printer_returns_string(self):
        self.assertEqual("test",  self.printer.print())

