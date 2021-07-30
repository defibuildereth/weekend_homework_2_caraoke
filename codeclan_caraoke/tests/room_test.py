import unittest
from classes.rooms import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("The Lounge")

    def test_room_has_name(self):
        self.assertEqual("The Lounge", self.room1.name)

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, self.room1.get_current_guest_count())