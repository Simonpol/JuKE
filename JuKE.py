import sys
from tkinter import *
# from tkinter import filedialog
window = Tk()
window.geometry('600x400+200+100')
window.resizable(0,0)
window.title("JuKE")
def generalContent():
    global general_body
    general_body = LabelFrame(window, text ="Basical",)
    general_body.pack(expand = True, fill = BOTH, padx=5, pady=5)

    # if (adOperationsContent):
    #     general_body.pack_forget()

def adOperationsContent():
    global adOperations_body
    adOperations_body = LabelFrame(text="ADOperations")
    adOperations_body.pack(expand = True, fill = BOTH, padx=5, pady=5)


    
        
# Menu bar with buttons

def generalbtn_click_button():
    global clicks
    clicks = 0
    clicks += 1
    if (clicks == 1):
        generalContent()
        adOperations_body.pack_forget()
        generalBtn.config(state = "disabled")
        adOperationsBtn.config(state = "normal")

     

def adoperationsbtn_click_button():
    clicks = 0
    clicks +=1
    if (clicks == 1):
        adOperationsContent()
        general_body.pack_forget()
        adOperationsBtn.config(state = "disabled")
        generalBtn.config(state = "normal")


menubar = Frame(window, bg = 'red', width = 600)
generalBtn = Button(menubar, relief = RAISED, text='General', command = generalbtn_click_button)
adOperationsBtn = Button(menubar, relief = RAISED, text = 'ADOperarions', command = adoperationsbtn_click_button)
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