from PIL import ImageTk, Image
from pystray import MenuItem as item
from playsound import playsound
import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray, GPUtil, webbrowser
pydir = os.path.dirname(os.path.realpath(__file__))
def mainwindow():
    global root
    global windowvisible
    windowvisible = True
    traymenu.update_menu()
    root = tkinter.Tk()
    root.wm_attributes("-transparentcolor", '#010110')
    #Stats
    tkinter.Label(root, text=f"Gpu: {gpuname['gpuname']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=30, width=400, height=50)
    tkinter.Label(root, text='Miner:', bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=80, width=400, height=50)
    tkinter.Label(root, text='Algo:', bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=130, width=400, height=50)
    tkinter.Label(root, text='Pool:', bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=180, width=400, height=50)
    tkinter.Label(root, text='Region:', bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=230, width=400, height=50)
    #middle
    tkinter.Canvas(root, bg="#2D2C36", highlightthickness=0).place(x=375,y=30,width=50,height=520)#temptemptemptemp
    tkinter.Label(root, text='100°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=30, width=50, height=30)
    tkinter.Label(root, text='60°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=275, width=50, height=30)
    tkinter.Label(root, text='20°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=520, width=50, height=30)
    #bottomright
    tkinter.Button(root,fg="white", text= "Start",bg="#222129", border=0, font=fontregular).place(x=375,y=550,width=425,height=50)
    tkinter.Label(root, text=f'{hashrate} mh/s', bg='#303136', fg="white", font=fontextremelybig).place(x=425, y=480, width=350, height=70)
    #top
    tkinter.Canvas(root, bg="#222129", highlightthickness=0).place(x=0,y=0,width=800,height=30)
    tkinter.Button(root, text='Settings', bg='#222129', fg="white", border=1, font=fontregular).place(x=0, y=0, width=188, height=30)
    tkinter.Button(root, text='Temperature Menu', bg='#222129', fg="white", border=1, font=fontregular).place(x=200, y=0, width=400, height=30)
    tkinter.Button(root, text='About us', bg='#222129', fg="white", border=1, font=fontregular, command=aboutus).place(x=612, y=0, width=188, height=30)


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
def aboutus():
    global about
    global aboutopen
    def openabout():
        global about
        def close():
            global aboutopen
            aboutopen = False
            about.destroy()
        def website(site):
            if site == 1:
                webbrowser.open("http://seflon.ddns.net/", new=2, autoraise=True)
            if site == 2:
                webbrowser.open("https://mezomgmt.com/", new=2, autoraise=True)
        about = tkinter.Toplevel()
        about.geometry("600x400")
        about.resizable(False, False)
        about.iconbitmap(f'{pydir}\\3060.ico')
        about.configure(bg='#303136')
        #About looks
        tkinter.Label(about, text="Fruit Salad,", font=fontbig, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=0)
        tkinter.Label(about, text="a Salad mining manager.", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=10, y=30)
        tkinter.Label(about, text="Made by Let Software", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=60)
        tkinter.Label(about, text="with help by Mezo#0001 from MezoMGMT", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=100)
        tkinter.Button(about, text="seflon.ddns.net", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(1)).place(x=150, y=60)
        tkinter.Label(about, text="Let Software:", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y= 140)
        tkinter.Label(about, text="Letronix624#9040 (Let)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 160)
        tkinter.Label(about, text="Nilsipilzi#9733 (brot)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 180)
        tkinter.Button(about, text="mezomgmt.com", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(2)).place(x=275, y=100)

        about.protocol("WM_DELETE_WINDOW", close)
    if not aboutopen:
        aboutopen = True
        threading.Thread(target=openabout).start()
    else:
        about.deiconify()
        about.focus()
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
def changegpu():
    global gpuname
    gpuname['gpuname'] = nvidia.get()
    with open(f"{pydir}\\settings.json", ("w")) as settings:
                settings.write(json.dumps(gpuname))
    gpudefine.destroy()
icon = Image.open(f"{pydir}\\3060.ico")
fontregular = (f"{pydir}\\BarlowCondensed-Medium.ttf", 10, "bold")
fontbig = (f"{pydir}\\BarlowCondensed-Medium.ttf", 20, "bold")
fontextremelybig = (f"{pydir}\\BarlowCondensed-Medium.ttf", 50, "bold")
a = ""
hashrate = 0
aboutopen = False
gpuname = {'gpuname':''}
gpus = GPUtil.getGPUs()
supportedgpus = [
    "GTX 1050",
    "GTX 1050 Ti",
    "GTX 1060",
    "GTX 1070",
    "GTX 1070 Ti",
    "GTX 1080",
    "GTX 1080 Ti",
    "GTX 1650",
    "GTX 1650 Super",
    "GTX 1660",
    "GTX 1660 Super",
    "GTX 1660 Ti",
    "RTX 2060",
    "RTX 2060 Super",
    "RTX 2070",
    "RTX 2070 Super",
    "RTX 2080",
    "RTX 2080 Super",
    "RTX 2080 Ti",
    "RTX 3050",
    "RTX 3060",
    "RTX 3060 Ti",
    "RTX 3070",
    "RTX 3070 Ti",
    "RTX 3080",
    "RTX 3080 TI",
    "RTX 3090",    
]
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item('Hide', windowclose, default=False),
    #item('Quit', byebye, default=False)
)
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)
if __name__ == "__main__":
    for gpu in gpus:
        gpuname['gpuname'] = gpu.name
    if gpuname['gpuname'] == "":
        try:
            with open(f"{pydir}\\settings.json", ("r")) as settings:
                gpuname['gpuname'] = json.load(settings)["gpuname"]
        except:
            gpuname['gpuname'] = "Unknown"
            gpudefine = tkinter.Tk()
            nvidia = tkinter.StringVar()
            nvidia.set("Nvidia")
            tkinter.Label(gpudefine, text=f'No GPU Detected. Select your GPU.', bg='#303136', fg="white", font=fontregular).pack()
            tkinter.OptionMenu(gpudefine, nvidia, *supportedgpus).pack()
            tkinter.Button(gpudefine, text="Select", command=changegpu).pack()

            gpudefine.title("Fruit Salad")
            gpudefine.iconbitmap(f'{pydir}\\3060.ico')
            gpudefine.geometry("600x400")
            gpudefine.resizable(False, False)
            gpudefine.configure(bg='#303136')
            gpudefine.mainloop()

    traythread = threading.Thread(target=trayicon)
    traythread.start()
    threading.Thread(target=mainwindow).start()