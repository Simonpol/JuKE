import sys
import os
import socket
import keyboard
from tkinter import *

ipaddress = socket.gethostbyname(socket.gethostname())
computername = os.environ['COMPUTERNAME']
username = os.environ['USERDOMAIN'] + '\\' + os.environ['USERNAME']
window = Tk()
window.geometry('600x400+200+100')
window.resizable(0,0)
window.title("JuKE")
def generalContent():

    global general_body
    general_body = LabelFrame(window, text ="Basical",)
    general_body.pack(expand = True, fill = BOTH, padx=5, pady=5)
    # System information field
    sysinfo_body = LabelFrame(general_body, text = "System Info", width = 200, height = 400)

    def computername_validate(new_value):
        return new_value == computername
    vcomcmd = (window.register(computername_validate), '%P')

    def username_validate(new_value):
        return new_value == username
    vusecmd = (window.register(username_validate), '%P')

    def ipaddress_validate(new_value):
        return new_value == ipaddress
    vipcmd = (window.register(ipaddress_validate), '%P')
    
                

    # Computer Name block

    com_infoblock = Frame( sysinfo_body, width =100, height = 10)
    com_infolabel = Label(com_infoblock, text = "Computer Name")
    com_computername = Entry(com_infoblock, justify = CENTER, fg = 'blue', validate = 'key', validatecommand = vcomcmd)
    com_computername.insert(0,computername)
    com_infolabel.pack(side = LEFT)
    com_computername.pack(side = RIGHT)
    com_infoblock.pack(padx =5, pady=5)
    
    # User Name block
    use_infoblock = Frame( sysinfo_body, width=100, height=10)
    use_infolabel = Label( use_infoblock, text="User Name           ")
    use_username = Entry(use_infoblock, justify = CENTER, fg = 'blue', validate = 'key', validatecommand = vusecmd)
    use_infolabel.pack(side = LEFT)
    use_username.pack(side = RIGHT)
    use_username.insert(0, username)
    use_infoblock.pack(padx=5, pady=5)

    # Ip address block
    ip_infoblock = Frame( sysinfo_body, width=100, height=100)
    ip_infolabel = Label( ip_infoblock, text = "IP-address            ")
    ip_ipaddress = Entry( ip_infoblock, justify=CENTER, fg='blue', validate = 'key', validatecommand = vipcmd)
    ip_ipaddress.insert(0, ipaddress)

    ip_infolabel.pack(side = LEFT)
    ip_ipaddress.pack(side = RIGHT)
    ip_infoblock.pack(padx=5, pady=5)

    

    # SysInfo block dispaying
    sysinfo_body.pack(padx=5, pady= 5, side = RIGHT, anchor = NE)
    

    
    
    

def adOperationsContent():
    global adOperations_body
    adOperations_body = LabelFrame(text="ADOperations")
    adOperations_body.pack(expand = True, fill = BOTH, padx=5, pady=5)


    
        
# Menu bar with buttons
# Action after clicking "General Buttons"

def generalbtn_click_button():
    global clicks
    clicks = 0
    clicks += 1
    if (clicks == 1):
        generalContent()
        adOperations_body.pack_forget()
        generalBtn.config(state = "disabled")
        adOperationsBtn.config(state = "normal")

     
# Actiond after "AdOperations" click button
def adoperationsbtn_click_button():
    clicks = 0
    clicks +=1
    if (clicks == 1):
        adOperationsContent()
        general_body.pack_forget()
        adOperationsBtn.config(state = "disabled")
        generalBtn.config(state = "normal")
# Menu bar
menubar = Frame(window, width = 600)
generalBtn = Button(menubar, relief = RAISED, text='General', command = generalbtn_click_button, state = DISABLED)
adOperationsBtn = Button(menubar, relief = RAISED, text = 'ADOperarions', command = adoperationsbtn_click_button)
menubar.pack(side = TOP, anchor = NW)
generalBtn.pack(side = LEFT)
adOperationsBtn.pack()
generalContent()
window.mainloop()