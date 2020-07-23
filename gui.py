from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Music")
root.geometry("500x300")
root.iconbitmap("music.ico")
root.config(background='#3498db')

frame = Frame(root, bg='#3498db')

def browseFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    print(root.filename)


button1 = Button(frame, text="Browse", bg='#1abc9c', fg="white", command=browseFile)
button1.pack()

frame.pack(expand=YES)

root.mainloop()
