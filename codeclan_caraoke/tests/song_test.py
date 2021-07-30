import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Livin' On A Prayer", "Bon Jovi", 180)

    def test_song_has_name(self):
        self.assertEqual("Livin' On A Prayer", self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Bon Jovi", self.song1.artist)

    def test_song_has_duration(self):
        self.assertEqual(180, self.song1.duration)