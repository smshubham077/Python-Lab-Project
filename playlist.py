class SongNode:
    # Represents one song.
    def __init__(self, title, artist, next=None, prev=None):
        self.title = title
        self.artist = artist
        self.next = next
        self.prev = prev

    def playlist_display(self): 
        return f"[{self.title}] - [{self.artist}]"


class Playlist:
    # Manages the list and navigation.
    def __init__(self):
        self.current = None
        self.start = None

    def is_empty(self):
        if self.current is None:
            return True
        else:
            return False

    def add_song(self, title, artist):
        new_song = SongNode(title, artist)

        if self.is_empty():
            new_song.next = new_song
            new_song.prev = new_song
            self.current = new_song
            self.start = new_song
            return f"Added {new_song.playlist_display()} as the first song in the playlist."
        else:
            # Insert the new song before the current one
            new_song.prev = self.current.prev
            new_song.next = self.current
            self.current.prev.next = new_song
            self.current.prev = new_song
            return f"Added {new_song.playlist_display()} to the playlist."
    
    def remove_song(self, title, artist):
        while self.current:
            if self.current.title == title:
                if self.current.next == self.current: # If there is only one song in the playlist.
                    self.current = None # Erase it in a simple manner.
                    self.start = None
                    return f"Removed {title} from the playlist. The playlist is now empty."
                else: # If there is more than one song in the playlist.
                    self.current.prev.next = self.current.next # The two shift together and essentially squeeze out that other node.
                    self.current.next.prev = self.current.prev # Same thing here.
                    if self.current == self.start: # If the current song was the start song, move the start to the next as well.
                        self.start = self.current.next
                        self.current = self.current.next # Now your focusing on the new head, not the old one.
                    else:
                        self.current = self.current.next # Just move current to the next song.
                    return f"Removed {title} from the playlist." # Either way, you return this message.
            self.current = self.current.next # Move to the next song if there is no match.
            if self.current == self.start: # If you have looped back to the start, break.
                break
        return f"Song titled {title} not found in the playlist." # If you exit the loop without finding it, return this message.

    def play_next(self):
        if self.is_empty():
            return "Playlist is empty."
        self.current = self.current.next 
        return "Now playing: {self.current.playlist_display()}"
        # When is next or prev defined as being the next or previous node? 
        # You define it when setting up the node by making it so that when you 
        # see 'prev' you go back and when you see 'next' you go forward.

    def play_previous(self):
        if self.is_empty():
            return "Playlist is empty."
        self.current = self.current.prev
        return "Now playing: {self.current.playlist_display()}"
    
    def display_playlist(self):
        playlist = []
        self.current = self.start # Start at the beginning of the playlist.

        while self.current:
            print(self.current.playlist_display()) # Print for each node it's title and artist.
            playlist.append(self.current.playlist_display()) # Add each node's title and artist to a list.
            self.current = self.current.next # Move to the next node.
            if self.current == self.start: # If we have looped back to the start, break.
                break # Since it's circular you need to put a stop to the looping.


    def show_current_song(self):
        while self.current:
            return self.current.playlist_display() # Return the current song's title and artist.