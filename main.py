import tkinter
import tkinter.font
#from page import Page

root = tkinter.Tk()

file = "test.html"

f = tkinter.font.Font(family="Helvetica", size=12)

l = tkinter.Label(root, text=file)
l.pack()

f = tkinter.font.nametofont(l["font"])
for i in ("family","size","weight", "slant", "underline", "overstrike"):
    print(i, repr(f[i]))

"""webpage = Page(root, file)
webpage.pack()"""

root.mainloop()