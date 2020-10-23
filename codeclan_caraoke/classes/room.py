import pdb
class Room:
    
    def __init__(self, room_name):
       self.room_name = room_name
       self.guests = []
       self.playlist = []
    
    def playlist(self):
        return self.playlist
    
    def add_to_playlist(self, song):
        if song not in self.playlist:
            self.playlist.append([song])
    #for loop, for song in self.playlist:
        

