class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def can_afford_entry(self, amount):
        return self.wallet >= amount

    def deduct_fee(self, amount):
        self.wallet -= amount

