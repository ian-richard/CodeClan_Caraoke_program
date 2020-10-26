class Song:

    def  __init__(self, song):
        self.song = song
        self.song_library = []
    
    # def song_library(self):
        
    def add_to_song_library(self, song):
        self.song_library.append([song])
    
    def remove_song_library(self, song):
        self.song_library.remove([song])
    
    # def print_library(self):
    #     for x in range(len(self.song_library)): 
    #         return self.song_library[x]

    
    

