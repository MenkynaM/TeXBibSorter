import tkinter as tk
# from tkinter import *
from tkinter import ttk, filedialog
import os
import BibSorter


class GUI:
    """ GUI for selecting a .tex file from the system
    """    
    

    def __init__(self):
        self.root = tk.Tk()
        self.file_loc = tk.StringVar()
        self.file_loc.set('File to be sorted')
        self.root.title("BibSorter")
        # self.root.geometry("300x100+20+20")
        style = ttk.Style()
        style.configure("TLabel", foreground="black", background="white")

        self.label = ttk.Label(self.root, textvariable=self.file_loc, font=("Ariel", 10))
        self.label.pack(padx=10, pady=10,fill=tk.BOTH, expand=True)
        self.label.configure(anchor="center")

        self.greet_button = ttk.Button(self.root, text="Choose a file", command=self.choose_file)
        self.greet_button.pack(side=tk.LEFT, pady=5, padx=5)

        self.close_button = ttk.Button(self.root, text="Sort!", command=self.sortit)
        self.close_button.pack(side=tk.RIGHT, pady=5, padx=5)
        self.root.mainloop()

    def choose_file(self):
        path = tk.filedialog.askopenfilename(
            initialdir = os.path.dirname(__file__),
            title = "Select file",
            filetypes = [("TeX files","*.tex"), ('All files','*.*')]
        )
        print(path)
        self.file_loc.set(path)
        self.root.update()

    def sortit(self):
        print(self.file_loc.get())
        bs = BibSorter.BibSorter()
        bs.sort(self.file_loc.get())

if __name__ == "__main__":
    my_gui = GUI()