Project Overview:

This project is a Music Playlist Manager developed using a Circular Doubly Linked List in Python. Each song in the playlist is stored as a node that contains the song title, artist name, a pointer to the next song, and a pointer to the previous song.

The circular doubly linked list structure allows smooth navigation between songs. Users can move to the next or previous song easily, and the playlist loops continuously from the last song back to the first.

The system provides a simple command-line interface (CLI) where users can manage their playlist interactively.

Features:

1] Add a new song to the playlist

2] Remove an existing song

3] Search for a song

4] Play the next song

5] Play the previous song

6] Show the current song

7] Display the entire playlist

8] Exit the application

How to Run the Project:

1] Make sure both files main.py and playlist.py are in the same folder.

2] Open the folder in VS Code or any Python IDE.

3] Run the program using main.py.

4] The command-line interface will appear, and you can start entering commands.

Example Usage:

Enter command: add_song
Enter title: Blinding Lights
Enter artist: The Weeknd
Added [Blinding Lights] - [The Weeknd] as the first song in the playlist.

Enter command: add_song
Enter title: Shape of You
Enter artist: Ed Sheeran
Added [Shape of You] - [Ed Sheeran] to the playlist.

Enter command: add_song
Enter title: Believer
Enter artist: Imagine Dragons
Added [Believer] - [Imagine Dragons] to the playlist.

Enter command: add_song
Enter title: Perfect
Enter artist: Ed Sheeran
Added [Perfect] - [Ed Sheeran] to the playlist.

Enter command: show_playlist
[Blinding Lights] - [The Weeknd]
[Shape of You] - [Ed Sheeran]
[Believer] - [Imagine Dragons]
[Perfect] - [Ed Sheeran]

Enter command: show_current_song
[Blinding Lights] - [The Weeknd]

Enter command: play_next
Current node: [Shape of You] - [Ed Sheeran]

Enter command: play_previous
Current node set to: [Blinding Lights] - [The Weeknd]

Enter command: remove_song
Enter title: Perfect
Removed Perfect from the playlist.

Enter command: show_playlist
[Blinding Lights] - [The Weeknd]
[Shape of You] - [Ed Sheeran]
[Believer] - [Imagine Dragons]

Enter command: exit
Exiting playlist manager.
Conclusion:

This project demonstrates the real-world application of circular doubly linked lists.
It helps in understanding dynamic memory allocation, insertion and deletion operations, and bidirectional traversal in data structures.
