import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Donald", 31)

    def test_guest_has_name(self):
        self.assertEqual("Donald", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(31, self.guest1.age)