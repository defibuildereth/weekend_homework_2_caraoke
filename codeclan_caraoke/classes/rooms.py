class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.capacity = capacity
        self.till = 0
        self.entry_fee = entry_fee

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
        if self.get_remaining_capacity() > 0:
            if guest.cash >= self.entry_fee:
                guest.reduce_cash(self.entry_fee)
                self.till += self.entry_fee
                self.guest_list.append(guest)
                self.capacity -= 1
        else:
            return "Room full!"

    def remove_guest(self, guest):
        self.guest_list.remove(guest)
        
    def get_remaining_capacity(self):
        return self.capacity

    def get_till(self):
        return self.till
