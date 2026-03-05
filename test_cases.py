from playlist import Playlist

def run_tests():
    playlist = Playlist()

    print("Adding Songs")
    print(playlist.add_song("Shape of You", "Ed Sheeran"))
    print(playlist.add_song("Believer", "Imagine Dragons"))

    print("\nDisplay Playlist")
    print(playlist.display_playlist())

    print("\nPlay Next")
    print(playlist.play_next())

    print("\nSearch Song")
    print(playlist.search_song("Believer"))

    print("\nRemove Song")
    print(playlist.remove_song("Shape of You", "Ed Sheeran"))

    print("\nFinal Playlist")
    print(playlist.display_playlist())

if __name__ == "__main__":
    run_tests()