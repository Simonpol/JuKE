import sys
from tkinter import *
from tkinter import filedialog
window = Tk()
window.title("JuKE")
explorerBtn = Button(window, text="Open")
explorerBtn.grid(column=1, row=0)
def explorerBtnAct(event):
    dirlist = filedialog.askdirectory()
explorerBtn.bind("<Button-1>", explorerBtnAct)
window.mainloop()