import sys
from tkinter import *
# from tkinter import filedialog
window = Tk()
window.geometry('600x400+200+100')
window.resizable(0,0)
window.title("JuKE")
def generalContent():
    general_body = LabelFrame(window, text ="Basical",)
    general_body.pack(expand = True, fill = BOTH, padx=5, pady=5)

def adOperationsContent():
    adOperations_body = LabelFrame(text="ADOperations")
    adOperations_body.pack(expand = True, fill = BOTH, padx=5, pady=5)

def isbuttonmenuPressed():
    print("hello")
        
# Menu bar with buttons
menubar = Frame(window, bg = 'red', width = 600)
generalBtn = Button(menubar, relief = RAISED, text='General', command = generalContent)
adOperationsBtn = Button(menubar, relief = RAISED, text = 'ADOperarions')
menubar.pack(side = TOP, anchor = NW)
generalBtn.pack(side = LEFT)
adOperationsBtn.pack()

# Кнопка поиска и событие при нажатии
# explorerBtn = Button(window, text="Open")
# explorerBtn.grid(column=1, row=0)
# def explorerBtnAct(event):
#     dirlist = filedialog.askdirectory()
# explorerBtn.bind("<Button-1>", explorerBtnAct)

window.mainloop()