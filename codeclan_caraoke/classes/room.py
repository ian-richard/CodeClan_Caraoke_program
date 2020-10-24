import pdb
class Room:
    
    def __init__(self, room_name):
       self.room_name = room_name
       self.guests = []
       self.playlist = []
    
    def playlist(self):
        return self.playlist
    
    def add_to_playlist(self, song):
        self.playlist.append([song])
   
    def remove_track_playlist(self, song):
       self.playlist.remove([song])

       #remove guest_list from guest class, add it to room. 
        

