import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Donald", 31, 100)

    def test_guest_has_name(self):
        self.assertEqual("Donald", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(31, self.guest1.age)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest1.cash)

    def test_reduce_cash(self):
        self.guest1.reduce_cash(20)
        self.assertEqual(80, self.guest1.cash)

