import tkinter as tk
from tkinter import filedialog, Text
import sys
import os

root = tk.Tk()
apps = []
filename = ''

os = sys.platform


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    if os == 'darwin':
        filename = filedialog.askopenfilename(
            initialdir="/applications", title="Select File")
        apps.append(filename)
    else:
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select File", filetypes=(("executables", "*.exe", ("all files", "*.*"))))
        apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()


canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="black", bg="white", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="black", bg="white")

runApps.pack()

root.mainloop()
