#import tkinter as tk

#root = tk.Tk()  #Това е прозореца на екрана
#root.title("secret documents")  #име на прозорец
#root.geometry('800x500') #това е размера мо

#label = tk.Label(root, text='secret documents', font=('Arial', 20))
#label.pack()

#textBox = tk.Text(root, height=10, font=('Arial', 15)) #това ти дава не ограничено пространство за писане
#textBox.pack(padx=20, pady=20) #padx-сширочината от ляво на дясно     pady-широчината от горе на доло

#entry = tk.Entry(root) #това е също то като горното ама не може на доло -----------------
#entry.pack() ---------------------

#but = tk.Button(root, text='DONT CLICK ME!', font=('Arial', 10)) #Бутон
#but.pack()

#butFrame = tk.Frame(root)
#butFrame.columnconfigure(0, weight=1)
#butFrame.columnconfigure(1, weight=1)  #-- Всичките тези ти дават да правиш колоните, ако си написал до две до две можеш
#butFrame.columnconfigure(2, weight=1)

#but1 = tk.Button(butFrame, text='1', font=('Arial', 10))
#but1.grid(row=0, column=0, sti=tk.W+tk.E)

#but2 = tk.Button(butFrame, text='2', font=('Arial', 10))
#but2.grid(row=0, column=1, sti=tk.W+tk.E)

#but3 = tk.Button(butFrame, text='3', font=('Arial', 10))
#but3.grid(row=0, column=2, sti=tk.W+tk.E)                  #--Това са самите колони, ако се чудиш защо са различни цифрите погледни
                                                           # в таблицата (ПРИМЕР 1) и ги сравни
#but4 = tk.Button(butFrame, text='4', font=('Arial', 10))
#but4.grid(row=1, column=0, sti=tk.W+tk.E)

#but5 = tk.Button(butFrame, text='5', font=('Arial', 10))
#but5.grid(row=1, column=1, sti=tk.W+tk.E)

#but6 = tk.Button(butFrame, text='6', font=('Arial', 10))
#but6.grid(row=1, column=2, sti=tk.W+tk.E)

#butFrame.pack(fill='x')

#   0  ,  1  ,  2  , и т-н.     ------ПРИМЕР 1
# 0 [1]    [2]    [3]
# ,
# 1 [4]    [5]    [6]
# ,
# 2 [7]    [8]    [9]
# и т-н.

#root.mainloop()

import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Tkinter GUI")

        self.label = tk.Label(self.root, text='Type please', font=('Arial', 20))
        self.label.pack(padx=10, pady=10)

        self.BoxTEXT = tk.Text(self.root, font=('Arial', 10))
        self.BoxTEXT.pack(padx=10, pady=10)

        self.CheckState = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 10), variable=self.CheckState)
        self.check.pack(padx=10, pady=10)

        self.root.mainloop()  # Стартира основния цикъл

if __name__ == "__main__":
    app = MyGUI()  # Инстанция на класа

    def show_message(self):
        if self.CheckState.get() == 0:
            print(self.BoxTEXT.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Massage", massage=self.BoxTEXT.get('1.0', tk.END))
MyGUI()
