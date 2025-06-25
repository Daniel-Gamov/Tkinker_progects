import tkinter as tk
import random
import winsound


root = tk.Tk()
root.title("Interactive counter with settings")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

num = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "brown", ]

label = tk.Label(root, text=f"The counter: {num}", font=("Courier", 30))
label.pack()

label2 = tk.Label(root, text="", font=("Courier", 30))
#entry.config(width=20)
label2.pack()

entry = tk.Entry(frame, font=("Courier", 20))
entry.pack(pady=15)


def add_1():
    global num
    num += 1
    label.config(text=f"The counter: {num}")


def reset():
    global num
    num = 0
    label.config(text=f"The counter: {num}")

def add_entry():
    global num
    try:
        value = int(entry.get())
        num += value
        label.config(text=f"The counter: {num}")
        label2.config(text="")
    except ValueError:
        label2.config(text="add a valid number!", fg="red")
        winsound.MessageBeep()

def random_color_generator():
    label.config(fg=random.choice(colors))

def subtract_1():
    global num
    num -= 1
    label.config(text=f"The counter: {num}")

def sound_play():
    winsound.MessageBeep()  # Може и winsound.Beep(1000, 150) за персонализиран звук




button1 = tk.Button(frame, text="Subtract 1",command=subtract_1, font=("Courier", 15))
button1.pack(side='left', padx=5)

button2 = tk.Button(frame, text="Add 1 to counter!",command=add_1, font=("Courier", 15))
button2.pack(side='left', padx=10)

button3 = tk.Button(root, text="Add entry to counter!",command=add_entry, font=("Courier", 15), fg="orange")
button3.pack()

button4 = tk.Button(root, text="random color!",command=random_color_generator, font=("Courier", 15), fg="brown")
button4.pack(pady=10)

button5 = tk.Button(root, text="reset the counter.", command=reset, font=("Courier", 15, ), fg="red")
button5.pack(pady=20)

root.mainloop()