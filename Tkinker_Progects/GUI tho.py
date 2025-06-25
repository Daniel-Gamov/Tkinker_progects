#import tkinter as tk
#import random

##root = tk.Tk()
#root.title("Colorful Counter")
#root.geometry('400x400')

#colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

#label = tk.Label(root, text="Click me!", font=("Comic Sans MS", 20), fg="black", bg="white")
#label.pack(pady=20)

#def random_color():
#    label.config(fg=random.choice(colors), bg=random.choice(colors))

#button = tk.Button(root, text="Change Color!", command=random_color, font=("Arial", 14))
#button.pack()

#root.mainloop()

#__________________________________

import tkinter as tk

root = tk.Tk()
root.title("Entry Box Example")
root.geometry("300x200")

# Създаване на поле за въвеждане (Entry)
entry = tk.Entry(root, font=("Courier", 14))
entry.pack(pady=10)

# Функция за вземане на текста
def show_text():
    text = entry.get()
    label.config(text=f"Въведен текст: {text}")

def delete():
    global entry
    entry.delete(0, tk.END)

def remove_3():
    global entry
    entry.delete(0, 3)

def remove_last_3():
    global entry
    lenth = len(entry.get())




# Бутон за показване на въведения текст
button = tk.Button(root, text="Покажи текста", command=show_text, font=("Courier", 12))
button.pack()

# Етикет за показване на резултата
label = tk.Label(root, text="Тук ще се покаже текстът!", font=("Courier", 12))
label.pack(pady=10)

button2 = tk.Button(root, text="Delete", command=delete, font=("Courier", 10))
button2.pack(padx=10)

button3 = tk.Button(root, text="Delete first 3", command=remove_3, font=("Courier", 10))
button3.pack(pady=25)

button4 = tk.Button(root, text="Delete the last 3", command=remove_last_3, font=("Courier", 10))
button4.pack(pady=10)

root.mainloop()