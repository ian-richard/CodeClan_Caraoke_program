class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.guest_list = []

    def add_to_guestlist(self, guest):
        self.guest_list.append([guest])
    
    def remove_guest_from_list(self, guest):
        self.guest_list.remove([guest])