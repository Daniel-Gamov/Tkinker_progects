
import tkinter as tk

root = tk.Tk()
root.title("Entry Box Example")
root.geometry("300x200")

# Creating an Entry Field
entry = tk.Entry(root, font=("Courier", 14))
entry.pack(pady=10)

# Text capture function
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




# Button to show entered text
button = tk.Button(root, text="Покажи текста", command=show_text, font=("Courier", 12))
button.pack()

# Result display label
label = tk.Label(root, text="Тук ще се покаже текстът!", font=("Courier", 12))
label.pack(pady=10)

button2 = tk.Button(root, text="Delete", command=delete, font=("Courier", 10))
button2.pack(padx=10)

button3 = tk.Button(root, text="Delete first 3", command=remove_3, font=("Courier", 10))
button3.pack(pady=25)

button4 = tk.Button(root, text="Delete the last 3", command=remove_last_3, font=("Courier", 10))
button4.pack(pady=10)

root.mainloop()
