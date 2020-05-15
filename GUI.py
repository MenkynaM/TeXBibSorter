import tkinter as tk
from tkinter import filedialog
import os

class GUI:
    def __init__(self, master):
        self.master = master
        self.myinit(self.master)

    def myinit(self, master):
        master.title("A simple GUI")

        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = tk.Button(master, text="Choose a file", command=self.choose_file)
        self.greet_button.pack(side=tk.LEFT)

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=tk.RIGHT)

    def greet(self):
        print("Greetings!")

    def choose_file(self):
        path = tk.filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
        )
        print(path)

root = tk.Tk()
my_gui = GUI(root)
root.mainloop()