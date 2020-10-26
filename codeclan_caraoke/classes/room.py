import pdb
class Room:
    
    def __init__(self, room_name, entry_fee):
       self.room_name = room_name
       self.guests = []
       self.playlist = []
       self.capacity = 6
       self._till = 0
       self._entry_fee = entry_fee
    
    def playlist(self):
        return self.playlist
    
    def add_to_playlist(self, song):
        self.playlist.append([song])
   
    def remove_track_playlist(self, song):
       self.playlist.remove([song])


    def add_guest_to_room(self, guest):
        if len(self.guests) < self.capacity and guest.can_afford_entry(self._entry_fee):
            guest.deduct_fee(self._entry_fee)
            self._till += self._entry_fee
            self.guests.append(guest)
        else:
            return "Room Full"
      
    def number_of_guests_in_room(self):
        return len(self.guests)


    def remove_guest_to_room(self, guest):
        self.guests.remove(guest)

    def get_capacity(self):
        return self.capacity
    
    def free_spaces(self):
        self.capacity - len(self.guests) 

    

        
        

