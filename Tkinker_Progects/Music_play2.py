import tkinter as tk

import pygame

pygame.mixer.init()

root = tk.Tk()
root.title("Music")
root.geometry("500x500")

label = tk.Label(root, text="Turn on the Music!")
label.pack(pady=5)

pygame.mixer.music.load("jazz-lounge-elevator-music-322314.mp3")

def play_sound():
    pygame.mixer_music.play(loops=0)
    label.config(text="Music is playing!")

def pause_music():
    pygame.mixer_music.pause()
    label.config(text="The Music is paused")

def unpause_music():
    pygame.mixer_music.unpause()
    label.config(text="The Music is unpaused")

def stop_music():
    pygame.mixer_music.stop()
    label.config(text="The Music is stopped")

button_play = tk.Button(root, text="PLAY",command=play_sound ,font=("Courier", 30))
button_play.pack(pady=5)

button_pause = tk.Button(root, text="Pause",command=pause_music ,font=("Courier", 20))
button_pause.pack(pady=5)

button_unpause = tk.Button(root, text="Unpause",command=unpause_music ,font=("Courier", 15))
button_unpause.pack(pady=5)

button_stop = tk.Button(root, text="Stop",command=stop_music ,font=("Courier", 20))
button_stop.pack(pady=5)

root.mainloop()