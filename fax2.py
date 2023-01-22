from tkinter import *
root = Tk()
root.title("My GUI with Scrollbar")
root.geometry("400x300")

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

# Create a Listbox
listbox = Listbox(root, yscrollcommand = scrollbar.set)

# Add some items to the Listbox
for i in range(500):
    listbox.insert(END, f"Item {i}")

listbox.pack(expand=True, fill='both')

# Configure the scrollbar to work with the Listbox
scrollbar.config(command = listbox.yview)

root.mainloop()

#for bill etc
