class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def get_current_guest_count(self):
        return len(self.guest_list)