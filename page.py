import json
import os
import tkinter as tk
import bs4

NODES = {}
files = [i if os.path.isfile("assets/nodes/"+i) for i in os.listdir('assets/nodes')]

class Node:
    def __init__(self, master, attrs, children, extras={}):
        self.master = master
        self.attrs = attrs
        self.children = children
        self.extras = extras

        self.widget = master
    
    def pack(self, **kwargs):
        pass


class Page(tk.Frame):
    def __init__(self, window, file):
        super().__init__(window)
        self.window = window
        self.parse(file)

    def parse(self, file):
        with open(file) as f:
            self.html_tree = bs4.BeautifulSoup()
        for child in self.html_tree.children:
            pass


