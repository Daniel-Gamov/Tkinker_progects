#import tkinter as tk # Импортираме библиотеката

#root = tk.Tk() #самия прозорец
#root.title("Първи Tkinter прозорец") # какво пише на прозорвца
#root.geometry("300x200")  # Размер на прозореца
#root.mainloop() # Стартираме главния цикъл на приложението

import tkinter as tk

root = tk.Tk()
root.title("The counter!")
root.geometry('400x400')

label = tk.Label(root, text="Counting...")
label.pack()

num = 0

def change_num():
    global num
    num += 1
    label.config(text=f"counter: {num}")

def reset():
    global num
    num = 0
    label.config(text=f"counter: 0")

def color():
    label.config(text=f"counter: {num}", fg="black", bg="red", font=("Comic Sans MS", 18))



label = tk.Label(root, text=f"counter: {num}", font=("Courier", 30))
label.pack(pady=20)

button1 = tk.Button(root, text="CliK me! ", command=change_num, font=("Courier", 14))
button1.pack()
button2 = tk.Button(root, text="reset ", command=reset, font=("Courier", 14))
button2.pack(pady=10)
button3 = tk.Button(root, text="color ", command=color, font=("Courier", 14, ))
button3.pack(pady=10)

root.mainloop()






