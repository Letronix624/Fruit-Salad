from PIL import ImageTk, Image
from tendo import singleton
from pystray import MenuItem as item
import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray

def mainwindow():
    global root
    global windowvisible
    windowvisible = True
    traymenu.update_menu()
    global root
    root = tkinter.Tk()
    root.title("Fruit Salad")
    root.iconbitmap(f'{pydir}\\3060.ico')
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(bg="orange")
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.protocol("WM_DELETE_WINDOW", windowclose)
    root.mainloop()
def trayicon():
    traymenu.run()
def windowclose():
    global windowvisible
    windowvisible = False
    root.withdraw()
def windowopen():
    global windowvisible
    if windowvisible:
        windowvisible = False
        root.withdraw()
    else:
        windowvisible = True
        root.deiconify()
fruitsaladsession = singleton.SingleInstance()
pydir = pydir = os.path.dirname(os.path.realpath(__file__))
icon = Image.open(f"{pydir}\\3060.ico")
a = ""
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item('Hide', windowclose, default=False,)
)
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)
if __name__ == "__main__":
    threading.Thread(target=trayicon).start()
    threading.Thread(target=mainwindow).start()
    while 1:
        a = input()
        if a == "show":
            root.deiconify()
        elif a == "hide":
            root.withdraw()
        else:
            print("Command doesn't exist")