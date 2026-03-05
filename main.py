import tkinter as tk
from playlist import Playlist

playlist = Playlist()

# Window setup
root = tk.Tk()
root.title("Music Playlist Management System")
root.geometry("520x700")   # height increase kiya
root.resizable(False, False)

# Title
tk.Label(root, text="🎵 Music Playlist Manager",
         font=("Arial", 18, "bold")).pack(pady=15)

# Song Title
tk.Label(root, text="Song Title").pack()
title_entry = tk.Entry(root, width=45)
title_entry.pack(pady=5)

# Artist
tk.Label(root, text="Artist").pack()
artist_entry = tk.Entry(root, width=45)
artist_entry.pack(pady=5)

# Output Box
output = tk.Text(root, height=15, width=60)
output.pack(pady=15)

# -------- FUNCTIONS -------- #

def clear_fields():
    title_entry.delete(0, tk.END)
    artist_entry.delete(0, tk.END)

def clear_output():
    output.delete(1.0, tk.END)

def add_song():
    result = playlist.add_song(title_entry.get(), artist_entry.get())
    output.insert(tk.END, result + "\n")
    clear_fields()

def remove_song():
    result = playlist.remove_song(title_entry.get(), artist_entry.get())
    output.insert(tk.END, result + "\n")
    clear_fields()

def play_next():
    output.insert(tk.END, playlist.play_next() + "\n")

def play_previous():
    output.insert(tk.END, playlist.play_previous() + "\n")

def show_current():
    output.insert(tk.END, playlist.show_current_song() + "\n")

def show_playlist():
    songs = playlist.display_playlist()
    output.insert(tk.END, "\n--- Playlist ---\n")
    if songs:
        for song in songs:
            output.insert(tk.END, song + "\n")
    else:
        output.insert(tk.END, "Playlist is empty.\n")

def search_song():
    result = playlist.search_song(title_entry.get())
    output.insert(tk.END, result + "\n")
    clear_fields()

# -------- BUTTONS -------- #

tk.Button(root, text="Add Song", width=25, command=add_song).pack(pady=4)
tk.Button(root, text="Remove Song", width=25, command=remove_song).pack(pady=4)
tk.Button(root, text="Play Next", width=25, command=play_next).pack(pady=4)
tk.Button(root, text="Play Previous", width=25, command=play_previous).pack(pady=4)
tk.Button(root, text="Show Current Song", width=25, command=show_current).pack(pady=4)
tk.Button(root, text="Show Playlist", width=25, command=show_playlist).pack(pady=4)
tk.Button(root, text="Search Song", width=25, command=search_song).pack(pady=4)
tk.Button(root, text="Clear Output", width=25, command=clear_output).pack(pady=4)
tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=10)

root.mainloop()