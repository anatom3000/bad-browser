import tkinter as tk

class Page(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window