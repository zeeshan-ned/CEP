import webbrowser
from tkinter import *


def open_html():
    webbrowser.open("index.html")


root = Tk()
button = Button(root, text="Open HTML", command=open_html)
button.pack()
root.mainloop()
