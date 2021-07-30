import unittest
from classes.rooms import Room
from classes.songs import Song
from classes.guests import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("The Lounge")
        self.song1 = Song("Livin' On A Prayer", "Bon Jovi", 180)
        self.guest1 = Guest("Donald", 31)


    def test_room_has_name(self):
        self.assertEqual("The Lounge", self.room1.name)

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, self.room1.get_current_guest_count())

    def test_room_has_empty_song_list(self):
        self.assertEqual(0, len(self.room1.song_list))

    def test_play_song(self):
        self.room1.play_song(self.song1)
        self.assertEqual("Livin' On A Prayer", self.room1.get_current_song())

    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, self.room1.get_current_guest_count())

    def test_remove_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.remove_guest(self.guest1)
        self.assertEqual(0, self.room1.get_current_guest_count())

    