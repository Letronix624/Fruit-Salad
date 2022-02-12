from PIL import ImageTk, Image
from pystray import MenuItem as item
from playsound import playsound
import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray
pydir = os.path.dirname(os.path.realpath(__file__))
def mainwindow():
    global root
    global windowvisible
    windowvisible = True
    traymenu.update_menu()
    root = tkinter.Tk()

    #middle
    tkinter.Canvas(root, bg="#2D2C36", highlightthickness=0).place(x=375,y=30,width=50,height=520)#temptemptemptemp
    tkinter.Label(root, text='100°C', bg='#2D2C36', fg="white").place(x=375, y=30, width=50, height=30)
    tkinter.Label(root, text='60°C', bg='#2D2C36', fg="white").place(x=375, y=275, width=50, height=30)
    tkinter.Label(root, text='20°C', bg='#2D2C36', fg="white").place(x=375, y=520, width=50, height=30)
    #bottomright
    tkinter.Button(root,fg="white", text= "Start",bg="#222129", border=0).place(x=375,y=550,width=425,height=50)
    #top
    tkinter.Canvas(root, bg="#222129", highlightthickness=0).place(x=0,y=0,width=800,height=30)
    tkinter.Button(root, text='Settings', bg='#222129', fg="white", border=1).place(x=0, y=0, width=188, height=30)
    tkinter.Button(root, text='Temperature Menu', bg='#222129', fg="white", border=1).place(x=200, y=0, width=400, height=30)
    tkinter.Button(root, text='About us', bg='#222129', fg="white", border=1).place(x=612, y=0, width=188, height=30)

    root.title("Fruit Salad")
    root.iconbitmap(f'{pydir}\\3060.ico')
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(bg='#303136')


    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.protocol("WM_DELETE_WINDOW", windowclose)
    root.mainloop()
    print('root dead')
def trayicon():
    traymenu.run()
    print('tray dead')
def megaguide():
    def mega():
        playsound(f"{pydir}\\MEGAGUIDE.mp3")
    threading.Thread(target=mega).start()
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
#def byebye():
    #root.destroy()
icon = Image.open(f"{pydir}\\3060.ico")
a = ""
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item('Hide', windowclose, default=False),
    #item('Quit', byebye, default=False)
)
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)
if __name__ == "__main__":
    traythread = threading.Thread(target=trayicon)
    traythread.start()
    threading.Thread(target=mainwindow).start()