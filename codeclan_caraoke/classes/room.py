import pdb
class Room:
    
    def __init__(self, room_name):
       self.room_name = room_name
       self.guests = []
       self.playlist = []
       self.capacity = 6
    
    def playlist(self):
        return self.playlist
    
    def add_to_playlist(self, song):
        self.playlist.append([song])
   
    def remove_track_playlist(self, song):
       self.playlist.remove([song])

       #remove guest_list from guest class, add it to room. 
       #see basic solution

    # def add_guest_to_room(self, guest):
    #     self.guests.append(guest)

    def add_guest_to_room(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "Room Full"


    def remove_guest_to_room(self, guest):
        self.guests.remove(guest)
    
    def capacity(self):
        len(self.guests) < self.capacity
        
        # if len(self.room.guests) is <6:
        #     return True

        

