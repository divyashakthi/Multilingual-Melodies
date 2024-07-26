# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import lyricsgenius
# import nltk
# from nltk.corpus import words
# from nltk.tokenize import word_tokenize
# import subprocess
# import datetime
# # from translate import Translator
# from googletrans import Translator, constants
# from pprint import pprint

# nltk.download('punkt')

# # Set up Spotify API client
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='174e4525132a4906a776c1e8212ba082',client_secret='92d2e5fb852442f0b8e59a3f197706c2'))


# def translate_to_english(text):
#     # translator = Translator(to_lang="en")
#     # english_lyrics = translator.translate(text)
#     # print(english_lyrics)
#     # return english_lyrics
#     translator = Translator()
#     translation = translator.translate(text)
#     print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# # Example usage:
# # lyrics = "Hola, cómo estás? Je suis bien. Ich liebe Musik."
# # english_lyrics = translate_to_english(lyrics)

# def get_track_id(song_name, artist_name):
#     results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')
#     if results['tracks']['items']:
#         return results['tracks']['items'][0]['id']
#     return None

# # Set up Genius API client
# genius = lyricsgenius.Genius('fvUgPzo-nDE2V_WzoQ82xdcmGujqtspipdIeS8aKMD9PuYqncnQiEYQEXIQ1uAah')

# def get_lyrics(track_id):
#     track = sp.track(track_id)
#     song_name = track['name']
#     artist_name = track['artists'][0]['name']
    
#     # Search for lyrics on Genius
#     song = genius.search_song(song_name, artist_name)
    
#     if song:
#         lyrics = song.lyrics
#         return lyrics
#     else:
#         return None
    
# # Define a function to check if a token is an English word
# nltk.download('words')
# english_words = set(words.words())

# def is_english_word(token):
#     return token.lower() in english_words

# #making a note
# def note(text):
#     d=datetime.datetime.now()
#     fn=str(d).replace("."," ").replace(":"," ")+" note.txt"
#     s = ""
#     for i in text:
#         if i.isalpha() or i=="\t" or i=="\n":
#             s+=i
#     print(s)
#     # with open(fn,"w") as f:
#     #     f.write(s)
#     # subprocess.Popen(["notepad.exe",fn])

# # Example usage
# # artist = "BTS"
# artist = str(input("Enter the name of the artist: "))
# # title = "Blood Sweat and Tears"
# title = str(input("Enter the name of the song: "))
# track_id = get_track_id(title, artist)
# lyrics = get_lyrics(track_id)
# # print(lyrics)
# # note(translate_to_english(lyrics))
# translate_to_english(lyrics)

import tkinter as tk
from tkinter import messagebox
from tkinter import font
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
from googletrans import Translator

nltk.download('punkt')
nltk.download('words')

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='174e4525132a4906a776c1e8212ba082',client_secret='92d2e5fb852442f0b8e59a3f197706c2'))

# Set up Genius API client
genius = lyricsgenius.Genius('fvUgPzo-nDE2V_WzoQ82xdcmGujqtspipdIeS8aKMD9PuYqncnQiEYQEXIQ1uAah')

def translate_to_english(text):
    # translator = Translator(to_lang="en")
    # english_lyrics = translator.translate(text)
    # print(english_lyrics)
    # return english_lyrics
    translator = Translator()
    translation = translator.translate(text)
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation

# Example usage:
# lyrics = "Hola, cómo estás? Je suis bien. Ich liebe Musik."
# english_lyrics = translate_to_english(lyrics)

def get_track_id(song_name, artist_name):
    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')
    if results['tracks']['items']:
        return results['tracks']['items'][0]['id']
    return None

# Set up Genius API client
genius = lyricsgenius.Genius('fvUgPzo-nDE2V_WzoQ82xdcmGujqtspipdIeS8aKMD9PuYqncnQiEYQEXIQ1uAah')

def get_lyrics(track_id):
    track = sp.track(track_id)
    song_name = track['name']
    artist_name = track['artists'][0]['name']
    
    # Search for lyrics on Genius
    song = genius.search_song(song_name, artist_name)
    
    if song:
        lyrics = song.lyrics
        return lyrics
    else:
        return None
    
# Define a function to check if a token is an English word
nltk.download('words')
english_words = set(words.words())

def is_english_word(token):
    return token.lower() in english_words

# Function to change the theme to dark mode with neon green highlights
def set_dark_theme():
    root.configure(bg="#000000")
    artist_label.configure(bg="#000000", fg="#00FF00")
    artist_entry.configure(bg="#333333", fg="#FFFFFF")
    title_label.configure(bg="#000000", fg="#00FF00")
    title_entry.configure(bg="#333333", fg="#FFFFFF")
    translate_button.configure(bg="#00FF00", fg="#000000")
    original_lyrics_button.configure(bg="#00FF00", fg="#000000")
    result_text.configure(bg="#333333", fg="#00FF00")

# Function to translate and display lyrics
def extract_lyrics_and_translate():
    artist = artist_entry.get()
    title = title_entry.get()

    if not artist or not title:
        messagebox.showinfo("Error", "Please enter both artist and title.")
        return

    track_id = get_track_id(title, artist)
    
    if not track_id:
        messagebox.showinfo("Error", "Track not found on Spotify.")
        return
    
    lyrics = get_lyrics(track_id)
    
    if not lyrics:
        messagebox.showinfo("Error", "Lyrics not found on Genius.")
        return

    english_lyrics = translate_to_english(lyrics)
    result_text.delete(1.0, tk.END)  # Clear the previous text
    result_text.insert(tk.END, english_lyrics)

# Function to show the original lyrics
def show_original_lyrics():
    artist = artist_entry.get()
    title = title_entry.get()

    if not artist or not title:
        messagebox.showinfo("Error", "Please enter both artist and title.")
        return

    track_id = get_track_id(title, artist)
    
    if not track_id:
        messagebox.showinfo("Error", "Track not found on Spotify.")
        return
    
    lyrics = get_lyrics(track_id)
    
    if not lyrics:
        messagebox.showinfo("Error", "Lyrics not found on Genius.")
        return
    
    result_text.delete(1.0, tk.END)  # Clear the previous text
    result_text.insert(tk.END, lyrics)
    # messagebox.showinfo("Original Lyrics", lyrics)

# Create the main application window
root = tk.Tk()
root.title("Lyrics Translator")
root.geometry("600x400")

# Create and configure the GUI elements
artist_label = tk.Label(root, text="Artist:")
artist_label.pack(pady=(20, 10))
artist_entry = tk.Entry(root)
artist_entry.pack(pady=(0, 10))

title_label = tk.Label(root, text="Title:")
title_label.pack(pady=(10, 10))
title_entry = tk.Entry(root)
title_entry.pack(pady=(0, 10))

translate_button = tk.Button(root, text="Translate", command=extract_lyrics_and_translate)
translate_button.pack(pady=(10, 10))

original_lyrics_button = tk.Button(root, text="Show Original Lyrics", command=show_original_lyrics)
original_lyrics_button.pack(pady=(10, 10))

# Create a custom font with the desired size
custom_font = font.nametofont("TkDefaultFont")
custom_font.configure(size=12)  # Adjust the size as needed

result_text = tk.Text(root, height=30, width=60, wrap=tk.WORD, font=custom_font)
result_text.pack(padx=20, pady=20)

# Set the initial dark theme
set_dark_theme()

# Start the GUI event loop
root.mainloop()
