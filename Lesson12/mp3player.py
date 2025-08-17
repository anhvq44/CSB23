class MP3player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None
        
    def add_song(self, song:str):
        self.music_queue.append(song)
        print(f"Added song: {song}")
        
    def play_song(self):
        if len(self.music_queue):
            self.current_song = self.music_queue.pop()
            print(f"Playing song: {self.current_song}")
        else:
            self.current_song = None
            print("The queue is empty.")
    
    def skip_song(self):
        if self.current_song:
            print(f"Skip song: {self.current_song}")
            self.play_song()
        else:
            print("No song is playing")
     