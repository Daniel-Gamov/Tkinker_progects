import tkinter as tk
import pygame

pygame.mixer.init()

pygame.mixer.music.load("jazz-lounge-elevator-music-322314.mp3")

root = tk.Tk()
root.title("Звукова програма")
root.geometry("300x150")

label = tk.Label(root, text="Натисни бутона!")
label.pack(pady=10)

def play_sound():
    pygame.mixer.music.play()
    label.config(text="Звукът се пусна!")

button = tk.Button(root, text="Пусни звук", command=play_sound)
button.pack()

# 5. Стартиране на прозореца
root.mainloop()










