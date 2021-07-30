class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []

    def get_current_guest_count(self):
        return len(self.guest_list)

    def get_current_song(self):
        if len(self.song_list) > 0:
            return self.song_list[0].name
        else:
            return "All quiet, play something!"

    def play_song(self, song):
        self.song_list.append(song)

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)
        
