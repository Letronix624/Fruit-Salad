version = "0.0.2"
import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray, webbrowser, sys, tkinter.messagebox, singleton, winsound, zipfile, win32gui, win32con
try:
    if not ".py" in sys.argv[0]:
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
except:
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
from tkinter import ttk
from pypresence import Presence
from PIL import ImageTk, Image
from pystray import MenuItem as item
pydir = os.path.dirname(os.path.realpath(__file__))
exedir = sys.executable
try: #only one instance
    FruitSaladSession = singleton.SingleInstance()
except:#error message
    os.startfile(f"{pydir}\\fail.vbs")
    os._exit(0)
try: #to get the name of the gpu
    gpunamerslkefjeslafjlska = subprocess.Popen(f"{os.environ['WINDIR']}\\System32\\nvidia-smi.exe --query-gpu=name --format=csv,nounits,noheader", stdout=subprocess.PIPE, shell=True)
    gpus = gpunamerslkefjeslafjlska.stdout.read().decode("UTF-8")[6:].replace("\r", "").replace(" GeForce ", "").split("\n")[:-1]
except: #no gpu
    gpus = []
del gpunamerslkefjeslafjlska
mining = False
class Lotfi(tkinter.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tkinter.StringVar()
        tkinter.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit() or self.get() == "" or self.get().startswith("-"): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)
def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value
def mainwindow():
    global hashratemonitor, tempnum, startbuttonanimation, tempbar, root, windowvisible, startbutton, globalworker, globalminer, globalalgo, globalpool, globalregion, hashrate, fontregular, fontbig, fontextremelybig, tempdisplaycomponents, miningtext
    windowvisible = True
    traymenu.update_menu()
    root = tkinter.Tk()
    root.configure(bg='#303136')
    with zipfile.ZipFile(f'{pydir}\\data\\.gui') as getimages:
        with getimages.open('On Switch 1.png', 'r') as data:
            im1 = data.read()
        with getimages.open('On Switch 2.png', 'r') as data:
            im2 = data.read()
        with getimages.open('On Switch 3.png', 'r') as data:
            im3 = data.read()
        with getimages.open('On Switch 4.png', 'r') as data:
            im4 = data.read()
        with getimages.open('On Switch 5.png', 'r') as data:
            im5 = data.read()
        with getimages.open('On Switch 6.png', 'r') as data:
            im6 = data.read()
        with getimages.open('On Switch 7.png', 'r') as data:
            im7 = data.read()
        with getimages.open('On Switch 8.png', 'r') as data:
            im8 = data.read()
        with getimages.open('On Switch 9.png', 'r') as data:
            im9 = data.read()
        with getimages.open('On Switch 10.png', 'r') as data:
            im10 = data.read()
        startbuttonanimation = [
            ImageTk.PhotoImage(data=im1, format='png'),
            ImageTk.PhotoImage(data=im2, format='png'),
            ImageTk.PhotoImage(data=im3, format='png'),
            ImageTk.PhotoImage(data=im4, format='png'),
            ImageTk.PhotoImage(data=im5, format='png'),
            ImageTk.PhotoImage(data=im6, format='png'),
            ImageTk.PhotoImage(data=im7, format='png'),
            ImageTk.PhotoImage(data=im8, format='png'),
            ImageTk.PhotoImage(data=im9, format='png'),
            ImageTk.PhotoImage(data=im10, format='png'),
            
        ]
    root.wm_attributes("-transparentcolor", '#010110')
    #Stats
    hashratemonitor = tkinter.Label(root, text=f'{hashrate} mh/s', bg='#303136', fg="white", font=fontextremelybig)
    hashratemonitor.place(x=425, y=480, width=350, height=70)
    shift = 0
    for gpu in gpus:
        tkinter.Label(root, text=f"{language['GPU:'][:-1]+str(gpus.index(gpu))}: {gpu}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=30+shift, width=400, height=50)
        shift = shift + 50
    globalminer = tkinter.Label(root, text=f"{language['Miner:']} {savedsettings['miner']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalminer.place(x=0, y=30+shift, width=400, height=50)
    globalalgo = tkinter.Label(root, text=f"{language['Algo:']} {savedsettings['algo']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalalgo.place(x=0, y=80+shift, width=400, height=50)
    globalpool = tkinter.Label(root, text=f"{language['Pool:']} {savedsettings['pool']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalpool.place(x=0, y=130+shift, width=400, height=50)
    globalworker = tkinter.Label(root, text=f"{language['Worker:']} {savedsettings['worker']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalworker.place(x=0, y=180+shift, width=400, height=50)
    globalregion = tkinter.Label(root, text=f"{language['Region:']} {savedsettings['region']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalregion.place(x=0, y=230+shift, width=400, height=50)
    #middle
    tkinter.Canvas(root, bg="#2D2C36", highlightthickness=0).place(x=375,y=30,width=50,height=520)#temptemptemptemp
    tempdisplaycomponents = [
        tkinter.Label(root, text='100°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='90°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='80°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='70°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='60°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='50°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='40°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='30°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='20°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='10°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Label(root, text='0°C', bg='#303136', fg="white", font=fontregular),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
        tkinter.Canvas(root, bg='#212126', highlightthickness=0),
    ]
    if savedsettings['tempbar']:
        tempdisplaycomponents[0].place(x=325, y=550-100*5.2, width=50, height=30)
        tempdisplaycomponents[1].place(x=325, y=550-92.5*5.2, width=50, height=30)
        tempdisplaycomponents[2].place(x=325, y=550-82.5*5.2, width=50, height=30)
        tempdisplaycomponents[3].place(x=325, y=550-72.5*5.2, width=50, height=30)
        tempdisplaycomponents[4].place(x=325, y=550-62.5*5.2, width=50, height=30)
        tempdisplaycomponents[5].place(x=325, y=550-52.5*5.2, width=50, height=30)
        tempdisplaycomponents[6].place(x=325, y=550-42.5*5.2, width=50, height=30)
        tempdisplaycomponents[7].place(x=325, y=550-32.5*5.2, width=50, height=30)
        tempdisplaycomponents[8].place(x=325, y=550-22.5*5.2, width=50, height=30)
        tempdisplaycomponents[9].place(x=325, y=550-12.5*5.2, width=50, height=30)
        tempdisplaycomponents[10].place(x=325, y=520, width=50, height=30)
        tempdisplaycomponents[11].place(x=370, y=550-90.25*5.2, width=60, height=2)
        tempdisplaycomponents[12].place(x=370, y=550-80.25*5.2, width=60, height=2)
        tempdisplaycomponents[13].place(x=370, y=550-70.25*5.2, width=60, height=2)
        tempdisplaycomponents[14].place(x=370, y=550-60.25*5.2, width=60, height=2)
        tempdisplaycomponents[15].place(x=370, y=550-50.25*5.2, width=60, height=2)
        tempdisplaycomponents[16].place(x=370, y=550-40.25*5.2, width=60, height=2)
        tempdisplaycomponents[17].place(x=370, y=550-30.25*5.2, width=60, height=2)
        tempdisplaycomponents[18].place(x=370, y=550-20.25*5.2, width=60, height=2)
        tempdisplaycomponents[19].place(x=370, y=550-10.25*5.2, width=60, height=2)
        
    tempbar = tkinter.Canvas(root, bg="red", highlightthickness=0)
    tempnum = tkinter.Label(root, bg="red", fg="white", font=fontregular)
    #bottom
    tkinter.Canvas(root, bg="#0A2133", highlightthickness=0).place(x=0, y=550 ,width=375, height=50)
    startbutton = tkinter.Label(root,fg="white",bg="#0A2133", font=fontregular, image=startbuttonanimation[9])
    startbutton.place(x=375,y=550,width=425,height=50)
    #top
    tkinter.Canvas(root, bg="#222129", highlightthickness=0).place(x=0,y=0,width=800,height=30)
    tkinter.Button(root, text=language['Settings'], bg='#222129', fg="white", border=1, font=fontregular, command=opensettings).place(x=0, y=0, width=188, height=30)
    tempdisplaycomponents.append(tkinter.Label(root, text=language['GPU Temperature'], bg='#222129', fg="white", font=fontregular))
    if savedsettings['tempbar']:
        tempdisplaycomponents[20].place(x=200, y=0, width=400, height=30)
    tkinter.Button(root, text=language['About us'], bg='#222129', fg="white", border=1, font=fontregular, command=aboutus).place(x=612, y=0, width=188, height=30)
    #miningarea
    tkinter.Button(root, text="cool round button with start\n on it and nice animation", font=fontregular, command=startminer).place(y=280, height=40, width=200, x=512)
    miningtext = tkinter.Label(root, text='Mining', font=fontbig, anchor=tkinter.W, background="black", foreground="yellow")
    miningtext.place(y=550, x=800, width=400, height=50)

    root.title("Fruit Salad")
    root.iconbitmap(f'{pydir}\\FuitSalad.ico')
    root.geometry("800x600")
    root.resizable(False, False)
    


    root.lift()
    root.focus()
    root.protocol("WM_DELETE_WINDOW", windowclose)
    root.mainloop()
    print('root stopped')
def rgb_to_hex(rgb): return '#%02x%02x%02x' % rgb
def preset(thething):
    match thething:
        case "Tesla K80":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
#>>>>>>> 74247baf046dbf523759d5b526d9b613f7ffce60
            savedsettings["oc"] = False
        case "GTX 1050":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -400
            savedsettings["mem"] = 550
            savedsettings["pl"] = 70
        case "GTX 1050 TI":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
#>>>>>>> 74247baf046dbf523759d5b526d9b613f7ffce60
            savedsettings["oc"] = True
            savedsettings["core"] = -400
            savedsettings["mem"] = 700
            savedsettings["pl"] = 70
        case "GTX 1060 3GB":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Autolykos2"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 100
            savedsettings["mem"] = 650
            savedsettings["pl"] = 100
        case "GTX 1060 6GB":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 100
            savedsettings["mem"] = 800
            savedsettings["pl"] = 80
        case "GTX 1070":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 170
            savedsettings["mem"] = 350
            savedsettings["pl"] = 97
        case "GTX 1070 TI":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 205
            savedsettings["mem"] = 740
            savedsettings["pl"] = 70
        case "GTX 1080":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 200
            savedsettings["mem"] = 800
            savedsettings["pl"] = 81
        case "GTX 1080 TI":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 60
            savedsettings["mem"] = 500
            savedsettings["pl"] = 90
        case "GTX 1650":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "kawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 150
            savedsettings["mem"] = 700
            savedsettings["pl"] = 100
        case "GTX 1650 SUPER":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "kawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 200
            savedsettings["mem"] = 1250
            savedsettings["pl"] = 90
        case "GTX 1660":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -300
            savedsettings["mem"] = 970
            savedsettings["pl"] = 65
        case "GTX 1660 SUPER":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 0
            savedsettings["mem"] = 1000
            savedsettings["pl"] = 62
        case "GTX 1660 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -200
            savedsettings["mem"] = 1125
            savedsettings["pl"] = 58
        case "RTX 2060":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 150
            savedsettings["mem"] = 1200
            savedsettings["pl"] = 75
        case "RTX 2060 SUPER": 
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 0
            savedsettings["mem"] = 1200
            savedsettings["pl"] = 67
        case "RTX 2070":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -502
            savedsettings["mem"] = 1150
            savedsettings["pl"] = 75
        case "RTX 2070 SUPER":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -502
            savedsettings["mem"] = 1200
            savedsettings["pl"] = 58
        case "RTX 2080":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -200
            savedsettings["mem"] = 1400
            savedsettings["pl"] = 63
        case "RTX 2080 SUPER":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 100
            savedsettings["mem"] = 1500
            savedsettings["pl"] = 70
        case "RTX 2080 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 196
            savedsettings["mem"] = 1186
            savedsettings["pl"] = 60
        case "Tesla P100":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
        case "Tesla V100":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
        case "RTX 3050":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
        case "RTX 3060":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -200
            savedsettings["mem"] = 1500
            savedsettings["pl"] = 70
        case "RTX 3060 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 0
            savedsettings["mem"] = 1250
            savedsettings["pl"] = 65
        case "RTX 3070":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 0
            savedsettings["mem"] = 1500
            savedsettings["pl"] = 60
        case "RTX 3070 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 0
            savedsettings["mem"] = 1600
            savedsettings["pl"] = 70
        case "RTX 3080":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -222
            savedsettings["mem"] = 1500
            savedsettings["pl"] = 69
        case "RTX 3080 TI":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -250
            savedsettings["mem"] = 1400
            savedsettings["pl"] = 84
        case "RTX 3090":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -200
            savedsettings["mem"] = 1500
            savedsettings["pl"] = 90
        case "Tesla T4":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
        case "A100 SXM4":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
def aboutus():#about us page
    global about
    global aboutopen
    def close():
        global aboutopen
        aboutopen = False
        about.destroy()
    def website(site):
        if site == 1:
            webbrowser.open("http://seflon.ddns.net/", new=2, autoraise=True)
        if site == 2:
            webbrowser.open("https://mezomgmt.com/", new=2, autoraise=True)
    if not aboutopen:
        aboutopen = True
        about = tkinter.Toplevel()
        about.title(language["About us"])
        about.geometry("600x400")
        about.resizable(False, False)
        about.iconbitmap(f'{pydir}\\FuitSalad.ico')
        about.configure(bg='#303136')
        #About looks
        tkinter.Label(about, text="Fruit Salad,", font=fontbig, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=0)
        tkinter.Label(about, text=language["a Salad mining tool."], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=10, y=30)
        tkinter.Label(about, text=language["Made by Let Software"], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=60)
        tkinter.Label(about, text=language["with help by Mezo#0001 from Mezo Management"], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=100)
        tkinter.Button(about, text="seflon.ddns.net", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(1)).place(x=450, y=60)
        tkinter.Label(about, text="Let Software:", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y= 140)
        tkinter.Label(about, text="Letronix624#9040 (Let)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 160)
        tkinter.Label(about, text="Nilsipilzi#9733 (brot)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 180)
        tkinter.Button(about, text="mezomgmt.com/fruitsalad", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(2)).place(x=450, y=100)
        about.protocol("WM_DELETE_WINDOW", close)
    else:
        about.deiconify()
        about.focus()
def opensettings():#settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings
    global settings
    global settingsopen
    global currentlyeditingmanual
    global editingwalleraddress
    global presetshift
    global editingtime
    currentlyeditingmanual = False
    editingwalleraddress = False
    editingtime = False
    if savedsettings['presetonoff']:
        presetshift = 0
    else:
        presetshift = 90
    def close():
        global settingsopen
        settingsopen = False
        settings.destroy()
    def openappsettings():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        appsettingsframe.place(x=0, y=30, width=800, height=570)
        a.configure(bg="#46464A")
        b.configure(bg="#222129")
        c.configure(bg="#222129")
        d.configure(bg=defaultbg)
        a.place_configure(height=40)
        b.place_configure(height=30)
        c.place_configure(height=30)
    def openminingsettings():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        miningsettingsframe.place(x=0, y=30, width=800, height=570)
        a.configure(bg="#222129")
        b.configure(bg="#46464A")
        c.configure(bg="#222129")
        d.configure(bg=defaultbg)
        a.place_configure(height=30)
        b.place_configure(height=40)
        c.place_configure(height=30)
    def openadvancedsettings():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        advancedsettingsframe.place(x=0, y=30, width=800, height=570)
        a.configure(bg="#222129")
        b.configure(bg="#222129")
        c.configure(bg="#46464A")
        d.configure(bg=defaultbg)
        a.place_configure(height=30)
        b.place_configure(height=30)
        c.place_configure(height=40)
    def openmegaguide():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        megaguidesettingsframe.place(x=0, y=30, width=800, height=570)
        a.configure(bg="#222129")
        b.configure(bg="#222129")
        c.configure(bg="#222129")
        d.configure(bg="pink")
        a.place_configure(height=30)
        b.place_configure(height=30)
        c.place_configure(height=30)
    def kickjesusfromchat():
        changelang("Furry")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////Big Thing Here//////////////////////////////////////////////////accept button happenings//////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def settingchange():#kaboooooooooooooooooooooooom ======================================================================
        global currentlyeditingmanual
        global editingwalleraddress
        global editingtime
        pllot.configure(state="normal")
        cclot.configure(state="normal")
        mclot.configure(state="normal")
        pllot.delete(0, "end")
        cclot.delete(0, "end")
        mclot.delete(0, "end")
        savedsettings["tempbar"] = selectedtempbar.get()
        savedsettings["presetonoff"] = selectedpreset.get()
        savedsettings["preset"] = selectedgpu.get()
        savedsettings["intensity"] = selectedintensity.get()
        savedsettings["fan:tonoff"] = selectedtempboundfanonoff.get()
        savedsettings["fanbool"] = selectedcustomfan.get()
        savedsettings["fan:t"] = selectedtempboundfan.get()
        savedsettings["updatetime"] = selectedhashrateupdatetime.get()
        savedsettings['fan'] = selectedfixedfan.get()
        savedsettings['oc'] = selectedoc.get()
        if currentlyeditingmanual:
            savedsettings['worker'] = givenworker.get()
            prelabel.configure(text=savedsettings['worker'])
            globalworker.configure(text=f"{language['Worker:']} {savedsettings['worker']}")
        if editingwalleraddress:
            savedsettings['wallet'] = givenwallet.get()
            prolabel.configure(text=savedsettings["ethwallet"])
        if editingtime:
            savedsettings['autostarttimer'] = givenstarttime.get()
            presetshitfters[1].configure(text=str(savedsettings['autostarttimer']))
        if savedsettings['presetonoff']:
            preset(savedsettings["preset"])
            if savedsettings['oc']:
                selectedoc.set(True)
                usecustomargscheck.select()
            else:
                selectedoc.set(False)
                usecustomargscheck.deselect()
        else:
            savedsettings['miner'] = selectedminer.get()
            savedsettings['algo'] = selectedalgo.get()
            savedsettings["pool"] = selectedpool.get()

        savedsettings['region'] = selectedregion.get()
        currentlyeditingmanual = False
        editingwalleraddress = False
        editingtime = False
        acceptbutton.place_forget()
        givenworker.place_forget()
        givenwallet.place_forget()
        givenstarttime.place_forget()
        manualworkergetterb.configure(state="normal")
        editwalletadress.configure(state="normal")
        presetshitfters[2].configure(state="normal")
        globalalgo.configure(text=f"{language['Algo:']} {savedsettings['algo']}")
        globalminer.configure(text=f"{language['Miner:']} {savedsettings['miner']}")
        globalpool.configure(text=f"{language['Pool:']} {savedsettings['pool']}")
        globalregion.configure(text=f"{language['Region:']} {savedsettings['region']}")
        prelabel.place(x=10, y=45, height=20, width=100)
        prolabel.place(x=5, y=45, width=250, height=20)
        presetshitfters[1].place(x=210, y=130 + presetshift, width=35, height=24)
        savedsettings['saladmining'] = selectedsaladmining.get()
        pllot.insert(tkinter.END, str(savedsettings["pl"]))
        cclot.insert(tkinter.END, str(savedsettings["core"]))
        mclot.insert(tkinter.END, str(savedsettings["mem"]))
        if savedsettings["presetonoff"]:
            pllot.configure(state="disabled")
            cclot.configure(state="disabled")
            mclot.configure(state="disabled")
        if selectedlang.get() != savedsettings["language"]:
            changelang(selectedlang.get())
        savesettings()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////Big Thing Here//////////////////////////////////////////////////accept button happenings//////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def enableaccept(aseggsaegsdg): #$$$$$$$$$$$$$
        global presetshift
        acceptbutton.place(x=595, y=565, width=200, height=30)
        if aseggsaegsdg == "saladmining":
            if selectedsaladmining.get():
                saladsettings.place(x=0, y=0, width=800, height=570)
                nonsaladsettings.place_forget()
            else:
                saladsettings.place_forget()
                nonsaladsettings.place(x=0, y=0, width=800, height=570)
        if selectedpreset.get():
            pllot.configure(state="disabled")
            cclot.configure(state="disabled")
            mclot.configure(state="disabled")
            ocsettings0.configure(state="disabled", troughcolor='grey')
            ocsettings1.configure(state="disabled")
            ocsettings2.configure(state="disabled")
            ocsettings3.configure(state="disabled", troughcolor='grey')
            ocsettings4.configure(state="disabled")
            ocsettings5.configure(state="disabled", troughcolor='grey')
        else:
            if selectedoc.get(): 
                state = "normal"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='lightgrey')
                ocsettings1.configure(state=state)
                if not selectedcustomfan.get(): state = "disabled"
                ocsettings2.configure(state=state)
                ocsettings4.configure(state=state)
                if selectedtempboundfanonoff.get(): 
                    ocsettings5.configure(state="normal", troughcolor='lightgrey')
                    ocsettings3.configure(state="disabled", troughcolor='grey')
                else:
                    ocsettings5.configure(state="disabled", troughcolor='grey')
                    ocsettings3.configure(state="normal", troughcolor='lightgrey')
            else: 
                state = "disabled"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='grey')
                ocsettings1.configure(state=state)
                ocsettings2.configure(state=state)
                ocsettings3.configure(state=state, troughcolor='grey')
                ocsettings4.configure(state=state)
                ocsettings5.configure(state=state, troughcolor='grey')
        if aseggsaegsdg == "preset":
            presetshitfters[2].configure(state="normal")
            presetshitfters[1].configure(text=str(savedsettings['autostarttimer']))
            givenstarttime.place_forget()
            if selectedpreset.get():
                usecustomargscheck.configure(state="disabled")
                pllot.configure(state="disabled")
                cclot.configure(state="disabled")
                mclot.configure(state="disabled")
                ocsettings0.configure(state="disabled", troughcolor='grey')
                ocsettings1.configure(state="disabled")
                ocsettings2.configure(state="disabled")
                ocsettings3.configure(state="disabled", troughcolor='grey')
                ocsettings4.configure(state="disabled")
                ocsettings5.configure(state="disabled", troughcolor='grey')
                h_haa.place(x=250, y=70, width=150, height=24)
                presetoffsettings.place_forget()
                presetshift = 0
                presetshitfters[0].place_configure(x=5, y=130 + presetshift, width=200, height=24)
                presetshitfters[1].place_configure(x=210, y=130 + presetshift, width=35, height=24)
                presetshitfters[2].place_configure(x=250, y=130 + presetshift, width=60, height=24)
                presetshitfters[3].place_configure(x=5, y=160 + presetshift, height=20, width=240)
                presetshitfters[4].place_configure(x=310, y=130 + presetshift, width=800, height=20)
                presetshitfters[5].place_configure(x=250, y=160 + presetshift, width=800, height=20)
                presetshitfters[6].place_configure(x=5, y=98 + presetshift, width=240, height=24)
                presetshitfters[7].place_configure(x=250, y=100 + presetshift, width=800, height=20)
                abcdefg.place_configure(y=70, x=410)
            else:
                usecustomargscheck.configure(state="normal")
                h_haa.place_forget()
                presetoffsettings.place(x=0, y=75, width=800, height=570)
                presetshift = 90
                presetshitfters[0].place_configure(x=5, y=130 + presetshift, width=200, height=24)
                presetshitfters[1].place_configure(x=210, y=130 + presetshift, width=35, height=24)
                presetshitfters[2].place_configure(x=250, y=130 + presetshift, width=60, height=24)
                presetshitfters[3].place_configure(x=5, y=160 + presetshift, height=20, width=240)
                presetshitfters[4].place_configure(x=310, y=130 + presetshift, width=800, height=20)
                presetshitfters[5].place_configure(x=250, y=160 + presetshift, width=800, height=20)
                presetshitfters[6].place_configure(x=5, y=98 + presetshift, width=240, height=24)
                presetshitfters[7].place_configure(x=250, y=100 + presetshift, width=800, height=20)
                abcdefg.place_configure(y=70, x=250)
        if aseggsaegsdg == "minersettings":
            hhhha['menu'].delete(0, 'end')
            hhhaa['menu'].delete(0, 'end')
            presetshitfters[6]['menu'].delete(0, 'end')
            for choice in mineralgos[selectedminer.get()]:
                hhhha['menu'].add_command(label=choice, command=tkinter._setit(selectedalgo, choice, lambda x:enableaccept("minersettings")))
            for choice in minerpools[selectedalgo.get()]:
                hhhaa['menu'].add_command(label=choice, command=tkinter._setit(selectedpool, choice, lambda x:enableaccept("minersettings")))
            for choice in minerregions[selectedpool.get()]:
                presetshitfters[6]['menu'].add_command(label=choice, command=tkinter._setit(selectedregion, choice, lambda x:enableaccept("minersettings")))
            if selectedalgo.get() not in mineralgos[selectedminer.get()]:
                selectedalgo.set(mineralgos[selectedminer.get()][0])
            if selectedpool.get() not in minerpools[selectedalgo.get()]:
                selectedpool.set(minerpools[selectedalgo.get()][0])
            if selectedregion.get() not in minerregions[selectedpool.get()]:
                selectedregion.set(minerregions[selectedpool.get()][0])
    def autoworkergetter():
        global currentlyeditingmanual
        currentlyeditingmanual = False
        givenworker.place_forget()
        prelabel.place(x=10, y=45, height=20, width=100)
        manualworkergetterb.configure(state="normal")
        try:
            autofoundwalletusername = False
            with open(f"{os.environ['appdata']}\\Salad\\logs\\main.log","r")as data:
                for line in data:
                    if 'worker ID:' in line:
                        savedsettings['worker'] = line[21:-1]
                        autofoundwalletusername = True
                    if '-wal salad -pass' in line:
                        savedsettings["prohashingpass"] = line.split()[line.split().index('-pass')+1]
            if not autofoundwalletusername:
                try:
                    with open(f"{os.environ['appdata']}\\Salad\\logs\\main.old.log","r")as data:
                        for line in data:
                            if 'worker ID:' in line:
                                savedsettings['worker'] = line[21:-1]
                                autofoundwalletusername = True
                        if '-wal salad -pass' in line:
                            savedsettings["prohashingpass"] = line.split()[line.split().index('-pass')+1]
                except:
                    pass
            if not autofoundwalletusername:
                tkinter.messagebox.showerror(title="No Wallet ID found.", message="You should mine a few minutes with Salad before pressing this Button.")
        except:
            tkinter.messagebox.showerror(title="Salad not installed", message="You need to install Salad from Salad.com to use this function.")
        globalworker.configure(text=f"{language['Worker:']} {savedsettings['worker']}")
        prelabel.configure(text=savedsettings['worker'], anchor=tkinter.W)
        savesettings()
    def manualworkergetter():
        global currentlyeditingmanual
        currentlyeditingmanual = True
        prelabel.place_forget()
        manualworkergetterb.configure(state="disabled")
        enableaccept(1)
        givenworker.place(x=10, y=45, height=20, width=100)
    def changewalletaddress():
        global editingwalleraddress
        editingwalleraddress = True
        prolabel.place_forget()
        editwalletadress.configure(state="disabled")
        enableaccept(1)
        givenwallet.place(x=5, y=45, width=250, height=20)
    def changeautostarttime():
        global editingtime
        global presetshift
        editingtime = True
        presetshitfters[1].place_forget()
        presetshitfters[2].configure(state="disabled")
        enableaccept(1)
        givenstarttime.place(x=210, y=100 + presetshift, width=35, height=24)
    def reset():
        PSYCHO_GROUPY_COCAIN_CRAZY = tkinter.messagebox.askokcancel(message=language["Are you sure you want to reset your settings?"], title="PSYCHO GROUPY COCAIN CRAZY", )
        if PSYCHO_GROUPY_COCAIN_CRAZY:
            os.remove(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json")
            restart()
    if not settingsopen:
        settingsopen = True
        settings = tkinter.Toplevel(bg=defaultbg)#PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY
        settings.title(language["Settings"])
        settings.geometry("800x600")
        settings.resizable(False, False)
        settings.iconbitmap(f'{pydir}\\FuitSalad.ico')
        settings.protocol("WM_DELETE_WINDOW", close)
        settings.bind("<Return>", lambda event:settingchange())
        #nice cock ----- Layout ----- settings layout. Mining settings, app settings, advanced settings, SECRET SETTINGS\\\\\ CIGARO CIGARO CIGAR
        appsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        miningsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        advancedsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        megaguidesettingsframe = tkinter.Frame(settings, bg="pink")
        appsettingsframe.place(x=0, y=30, width=800, height=570)
        a = tkinter.Button(settings, text=language["App Settings"], font=fontregular, bg='#46464A', fg="white", command=openappsettings, anchor=tkinter.S)
        a.place(x=0, y=0, width=300, height=40)
        b = tkinter.Button(settings, text=language["Mining Settings"], font=fontregular, bg='#222129', fg="white", command=openminingsettings, anchor=tkinter.S)
        b.place(x=300, y=0, width=300, height=30)
        c = tkinter.Button(settings, text=language["Advanced Settings"], font=fontregular, bg='#222129', fg="white", command=openadvancedsettings, anchor=tkinter.S)
        c.place(x=600, y=0, width=200, height=30)
        d = tkinter.Button(settings, border=0, bg=defaultbg, command=openmegaguide)
        d.place(x=790, y=590, width=10, height=10)
        acceptbutton = tkinter.Button(settings, text=language['Accept Settings'], command=settingchange)


        #App Settings
        """
        todo:
            Add Profiles
        """
            #vars
        selectedlang = tkinter.StringVar()
        selectedlang.set(savedsettings['language'])
        selectedtempbar =tkinter.BooleanVar()
        selectedtempbar.set(savedsettings['tempbar'])
        selectedminer = tkinter.StringVar()
        
            #looks
        hhhh = tkinter.OptionMenu(appsettingsframe, selectedlang, *supportedlanguages, command=enableaccept)
        hhhh.place(x=5, y=13, width=100, height=24)
        hhhh.configure(highlightthickness=0)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Language. When applying program will restart."], anchor=tkinter.W).place(x=110, y=15, width=800, height=20)
        tempcheckbutton = tkinter.Checkbutton(appsettingsframe, onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg=defaultbg, variable=selectedtempbar, activebackground=defaultbg, fg="black")
        tempcheckbutton.place(x=5, y=45)
        if gpus == []:
            tempcheckbutton.configure(state="disabled")
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=f"{language['Temperature Bar']} | {language['When checked the temperature bar is visible.']}", anchor=tkinter.W).place(x=40, y=47, width=800, height=20)
        tkinter.Button(appsettingsframe, bg="red", text=language["RESET EVERYTHING"], command=reset).place(x=5, y=80, height=20)

        #Mining Settings
            #vars
        selectedsaladmining =tkinter.BooleanVar()
        selectedsaladmining.set(savedsettings['saladmining'])
        selectedminer.set(savedsettings['miner'])
        selectedalgo = tkinter.StringVar()
        selectedalgo.set(savedsettings['algo'])
        selectedpool = tkinter.StringVar()
        selectedpool.set(savedsettings['pool'])
        selectedpreset =tkinter.BooleanVar()
        selectedpreset.set(savedsettings['presetonoff'])
        selectedgpu = tkinter.StringVar()
        selectedgpu.set(savedsettings['preset'])
        selectedregion = tkinter.StringVar()
        selectedregion.set(savedsettings['region'])

            #looks
        saladsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        nonsaladsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        presetoffsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        tkinter.Checkbutton(miningsettingsframe, text=language["Salad Mining?"], onvalue=True, offvalue=False, command=lambda:enableaccept("saladmining"), bg="#46464A", variable=selectedsaladmining, activebackground=defaultbg, fg="black").place(x=5, y=15, width=240)
        tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Should the miner mine to your Salad balance or an external wallet?"], anchor=tkinter.W).place(x=250, y=15, width=800, height=20)
        
            #salad
        prelabel = tkinter.Label(saladsettings, text=savedsettings['worker'], anchor=tkinter.W)
        manualworkergetterb = tkinter.Button(saladsettings, text=language['Manually set worker'],font=fontregular, command=manualworkergetter)
        givenworker = tkinter.Entry(saladsettings)
        prelabel.place(x=10, y=45, height=20, width=100)
        tkinter.Button(saladsettings, text=language['Auto get worker'],font=fontregular, command=autoworkergetter).place(x=120, y=45, height=20, width=180)
        manualworkergetterb.place(x=310, y=45, height=20, width=180)
        tkinter.Label(saladsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Worker to send the balance to.'], anchor=tkinter.W).place(x=500, y=45, width=800, height=20)
            #miner
        if savedsettings['saladmining']: saladsettings.place(x=0, y=0, width=800, height=570)
        else: nonsaladsettings.place(x=0, y=0, width=800, height=570)

        prolabel = tkinter.Label(nonsaladsettings, text=savedsettings['ethwallet'], anchor=tkinter.W)
        editwalletadress = tkinter.Button(nonsaladsettings, text=language['Edit'],font=fontregular, command=changewalletaddress)
        givenwallet = tkinter.Entry(nonsaladsettings)
        prolabel.place(x=5, y=45, width=250, height=20)
        editwalletadress.place(x=260, y=45, width=60, height=20)
        tkinter.Label(nonsaladsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Wallet address'], anchor=tkinter.W).place(x=330, y=45, width=800, height=20)

        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Miner:'][0:-1], anchor=tkinter.W).place(x=250, y=25, width=800, height=20)
        hhh = tkinter.OptionMenu(presetoffsettings, selectedminer, command=lambda x:enableaccept("minersettings"), *supportedminers) ##########################
        
        hhh.configure(highlightthickness=0)
        hhh.place(x=5, y=23, width=240, height=24)
        hhhha = tkinter.OptionMenu(presetoffsettings, selectedalgo, command=lambda x:enableaccept("minersettings"), *mineralgos[selectedminer.get()]) ###############################
        hhhha.configure(highlightthickness=0)
        hhhha.place(x=5, y=53, width=240, height=24)
        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Algo:'][0:-1], anchor=tkinter.W).place(x=250, y=55, width=800, height=20)
        hhhaa = tkinter.OptionMenu(presetoffsettings, selectedpool, command=lambda x:enableaccept("minersettings"), *minerpools[selectedalgo.get()]) ###############################
        hhhaa.configure(highlightthickness=0)
        hhhaa.place(x=5, y=83, width=240, height=24)
        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Pool:'][0:-1], anchor=tkinter.W).place(x=250, y=85, width=800, height=20)
        tkinter.Checkbutton(miningsettingsframe, text=language["Use preset"], onvalue=True, offvalue=False, command=lambda:enableaccept("preset"), bg="#46464A", variable=selectedpreset, activebackground=defaultbg, fg="black").place(x=5, y=70, width=240)
        #Use best settings premade for specified GPU.
        abcdefg = tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Use best settings premade for specified GPU.'], anchor=tkinter.W)
        if savedsettings['presetonoff']:
            abcdefg.place(y=70, x=410)
        else:
            abcdefg.place(y=70, x=250)
        h_haa = tkinter.OptionMenu(miningsettingsframe, selectedgpu, command=enableaccept, *supportedgpus)
        h_haa.configure(highlightthickness=0)
        if savedsettings['presetonoff']: h_haa.place(x=250, y=71, width=150, height=24)
        else: presetoffsettings.place(x=0, y=75, width=800, height=570)
        presetshitfters = [
            tkinter.Checkbutton(miningsettingsframe, text=language["Auto start"], onvalue=True, offvalue=False, command=lambda:enableaccept("p"), bg="#46464A", activebackground=defaultbg, fg="black"),
            tkinter.Label(miningsettingsframe, text=str(savedsettings['autostarttimer']), anchor=tkinter.W),
            tkinter.Button(miningsettingsframe, text=language['Edit'], command=changeautostarttime),
            tkinter.Button(miningsettingsframe, text=language['Scheduled mining settings'],font=fontregular),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Autostart and how many seconds for it to start.'], anchor=tkinter.W),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Opens the settings to a schedule menu.'], anchor=tkinter.W),
            tkinter.OptionMenu(miningsettingsframe, selectedregion, command=lambda x:enableaccept("minersettings"), *minerregions[selectedpool.get()]),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Region:'][:-1], anchor=tkinter.W),
        ]
        givenstarttime = Lotfi(miningsettingsframe)
        presetshitfters[0].place(x=5, y=130 + presetshift, width=200, height=24)
        presetshitfters[1].place(x=210, y=130 + presetshift, width=35, height=24)
        presetshitfters[2].place(x=250, y=130 + presetshift, width=60, height=24)
        presetshitfters[3].place(x=5, y=160 + presetshift, height=20, width=240)
        presetshitfters[4].place(x=310, y=130 + presetshift, width=800, height=20)
        presetshitfters[5].place(x=250, y=160 + presetshift, width=800, height=20)
        presetshitfters[6].place(x=5, y=98 + presetshift, width=240, height=24)
        presetshitfters[6].configure(highlightthickness=0)
        presetshitfters[7].place(x=250, y=100 + presetshift, width=800, height=20)
        #Advanced Settings - lets start
        selectedoc = tkinter.BooleanVar()
        selectedoc.set(savedsettings["oc"])
        selectedintensity = tkinter.IntVar()
        selectedintensity.set(savedsettings["intensity"])
        selectedtempboundfanonoff = tkinter.BooleanVar()
        selectedtempboundfanonoff.set(savedsettings["fan:tonoff"])
        selectedcustomfan = tkinter.BooleanVar()
        selectedcustomfan.set(savedsettings["fanbool"])
        selectedtempboundfan = tkinter.IntVar()
        selectedtempboundfan.set(savedsettings["fan:t"])
        selectedhashrateupdatetime = tkinter.IntVar()
        selectedhashrateupdatetime.set(savedsettings["updatetime"])
        selectedfixedfan = tkinter.IntVar()
        selectedfixedfan.set(savedsettings["fan"])
        """
        Contents:
        Overclock [V] Unlocks OC settings. (Know what you are doing...)
        shown when oc = True
        [   input   ] Power Limit
        [   input   ] Core Clock
        [   input   ] Memory Clock
        [Slider----O] 8 - 25 Intensity
        (V) Fixed fan speed
        shows when radio button above is checked -[Slider----O] 0% - 100% Fan Speed. (Careful)
        (V) Temp bound fan speed
        same - [Slider----O] 0c - 90c
        Slider--O] update rate for hashrate in seconds 5 - 60 seconds. --gpu-report-interval (default 5)
        [ Button ] Open logs
        """
        if savedsettings["presetonoff"]: ocstate = "disabled"
        else: ocstate = "normal"
        usecustomargscheck = tkinter.Checkbutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, variable=selectedoc, onvalue=True, state=ocstate, offvalue=False, command=lambda:enableaccept(''))
        usecustomargscheck.place(x=5, y=12)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Overclock GPU'] + " | " + language['Unlocks Overclock settings. (Know what you are doing!)'], anchor=tkinter.W).place(x=40, y=15, width=800, height=20)
        pllot = Lotfi(advancedsettingsframe)
        cclot = Lotfi(advancedsettingsframe)
        mclot = Lotfi(advancedsettingsframe)
        pllot.insert(tkinter.END, str(savedsettings["pl"]))
        cclot.insert(tkinter.END, str(savedsettings["core"]))
        mclot.insert(tkinter.END, str(savedsettings["mem"]))
        pllot.configure(state=ocstate)
        cclot.configure(state=ocstate)
        mclot.configure(state=ocstate)
        pllot.place(x=5, y=45, width=30, height=20)
        cclot.place(x=5, y=75, width=30, height=20)
        mclot.place(x=5, y=105, width=30, height=20)
        ocsettings0 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, state=ocstate, font=fontregular, variable=selectedintensity, from_=8, to=25, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings0.place(x=5, y=125, width=240)
        ocsettings1 = tkinter.Checkbutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, state=ocstate, variable=selectedcustomfan, onvalue=True, offvalue=False, command=lambda:enableaccept(''))
        ocsettings1.place(x=5, y=165)
        ocsettings2 = tkinter.Radiobutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, state=ocstate, variable=selectedtempboundfanonoff, value=False, command=lambda:enableaccept(''))
        ocsettings2.place(x=5, y=195)
        ocsettings3 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, state=ocstate, font=fontregular, variable=selectedfixedfan, from_=0, to=100, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings3.place(x=5, y=215, width=240)
        ocsettings4 = tkinter.Radiobutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, state=ocstate, variable=selectedtempboundfanonoff, value=True, command=lambda:enableaccept(''))
        ocsettings4.place(x=5, y=257)
        ocsettings5 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, state=ocstate, font=fontregular, variable=selectedtempboundfan, from_=0, to=90, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings5.place(x=5, y=275, width=240)
        tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, font=fontregular, variable=selectedhashrateupdatetime, from_=5, to=60, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept).place(x=5, y=345, width=240)
        tkinter.Button(advancedsettingsframe, text=language['Open miner logs'], command=lambda:os.startfile(pydir+"\\logs.txt")).place(x=5, y=390)



        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Power Limit"], anchor=tkinter.W).place(x=40, y=45, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Core Clock"], anchor=tkinter.W).place(x=40, y=75, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Memory Clock"], anchor=tkinter.W).place(x=40, y=105, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Intensity"], anchor=tkinter.W).place(x=250, y=142, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Custom fan speed"], anchor=tkinter.W).place(x=40, y=167, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Fixed fan speed"], anchor=tkinter.W).place(x=40, y=197, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Target fan speed in RPM"], anchor=tkinter.W).place(x=250, y=232, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Temp bound fan speed"], anchor=tkinter.W).place(x=40, y=260, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Target temperature in C"], anchor=tkinter.W).place(x=250, y=292, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Hashrate update frequency in seconds"], anchor=tkinter.W).place(x=250, y=362, width=800, height=20)
        #Megaguide Settings
        tkinter.Label(megaguidesettingsframe, text=language["Secret Settings"], bg="pink", fg="white", font=fontextremelybig).pack()
        tkinter.Button(megaguidesettingsframe, text="Megaguide", bg="Red", fg="White", command=megaguide, font=fontregular, padx=10, pady=5).pack(anchor=tkinter.NW)
        if savedsettings['language'] != "Furry":
            tkinter.Label(megaguidesettingsframe, text=language["Button below restarts the program."], font=fontregular).pack(anchor=tkinter.NW)
            hhh = tkinter.Button(megaguidesettingsframe, text=language["Furry Language"], bg="yellow", fg="pink", font=fontregular, command=kickjesusfromchat)
            hhh.pack(anchor=tkinter.NW) #messageinblood
        #finishing touch
        if selectedpreset.get():
            pllot.configure(state="disabled")
            cclot.configure(state="disabled")
            mclot.configure(state="disabled")
            ocsettings0.configure(state="disabled", troughcolor='grey')
            ocsettings1.configure(state="disabled")
            ocsettings2.configure(state="disabled")
            ocsettings3.configure(state="disabled", troughcolor='grey')
            ocsettings4.configure(state="disabled")
            ocsettings5.configure(state="disabled", troughcolor='grey')
        else:
            if selectedoc.get(): 
                state = "normal"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='lightgrey')
                ocsettings1.configure(state=state)
                if not selectedcustomfan.get(): state = "disabled"
                ocsettings2.configure(state=state)
                ocsettings4.configure(state=state)
                if selectedtempboundfanonoff.get(): 
                    ocsettings5.configure(state="normal", troughcolor='lightgrey')
                    ocsettings3.configure(state="disabled", troughcolor='grey')
                else:
                    ocsettings5.configure(state="disabled", troughcolor='grey')
                    ocsettings3.configure(state="normal", troughcolor='lightgrey')
            else: 
                state = "disabled"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='grey')
                ocsettings1.configure(state=state)
                ocsettings2.configure(state=state)
                ocsettings3.configure(state=state, troughcolor='grey')
                ocsettings4.configure(state=state)
                ocsettings5.configure(state=state, troughcolor='grey')
        
    else:
        settings.deiconify()
        settings.focus()
def megaguide():
    winsound.PlaySound(pydir+"\\MEGAGUIDE.wav", winsound.SND_ASYNC)
def windowclose():
    global windowvisible
    windowvisible = False
    root.withdraw()
done = True
def startminer():
    def t():
        global mining
        global miningtext
        global done
        done = False
        if mining:
            mining = False
            miningtext.place_configure(x=680)
            startbutton.configure(image=startbuttonanimation[1])
            time.sleep(0.05)
            miningtext.place_configure(x=700)
            startbutton.configure(image=startbuttonanimation[2])
            time.sleep(0.05)
            miningtext.place_configure(x=720)
            startbutton.configure(image=startbuttonanimation[3])
            time.sleep(0.05)
            miningtext.place_configure(x=740)
            startbutton.configure(image=startbuttonanimation[4])
            time.sleep(0.05)
            miningtext.place_configure(x=760)
            startbutton.configure(image=startbuttonanimation[5])
            time.sleep(0.05)
            miningtext.place_configure(x=780)
            startbutton.configure(image=startbuttonanimation[6])
            time.sleep(0.05)
            miningtext.place_configure(x=800)
            startbutton.configure(image=startbuttonanimation[7])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[8])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[9])
            time.sleep(0.05)
        else:
            mining = True
            startbutton.configure(image=startbuttonanimation[8])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[7])
            time.sleep(0.05)
            miningtext.place_configure(x=800)
            startbutton.configure(image=startbuttonanimation[6])
            time.sleep(0.05)
            miningtext.place_configure(x=780)
            startbutton.configure(image=startbuttonanimation[5])
            time.sleep(0.05)
            miningtext.place_configure(x=760)
            startbutton.configure(image=startbuttonanimation[4])
            time.sleep(0.05)
            miningtext.place_configure(x=720)
            startbutton.configure(image=startbuttonanimation[3])
            time.sleep(0.05)
            miningtext.place_configure(x=700)
            startbutton.configure(image=startbuttonanimation[2])
            time.sleep(0.05)
            miningtext.place_configure(x=680)
            startbutton.configure(image=startbuttonanimation[1])
            time.sleep(0.05)
            miningtext.place_configure(x=660)
            startbutton.configure(image=startbuttonanimation[0])
            time.sleep(0.05)
        done=True
    if done:
        threading.Thread(target=t).start()
def windowopen():
    global windowvisible
    if windowvisible:
        windowvisible = False
        root.withdraw()
    else:
        windowvisible = True
        root.deiconify()
def byebye(): #quit quit quit quit
    global quitter
    global windowvisible
    windowvisible = False
    quitter = True
    traymenu.visible = False
    traymenu.stop()
    os._exit(0)
def restart():
    os.startfile(sys.executable)
    traymenu.visible = False
    os._exit(0)
def savesettings():
    global tempdisplaycomponents
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
        settings.write(json.dumps(savedsettings))
    if savedsettings["tempbar"]:
        gputemperature = gputemp()
        tempnum.place(x=380,y=int(550-gputemperature*5.2),width=40,height=30)
        tempbar.place(x=380,y=int(550-gputemperature*5.2),width=40,height=520)
        tempdisplaycomponents[0].place(x=325, y=550-100*5.2, width=50, height=30)
        tempdisplaycomponents[1].place(x=325, y=550-92.5*5.2, width=50, height=30)
        tempdisplaycomponents[2].place(x=325, y=550-82.5*5.2, width=50, height=30)
        tempdisplaycomponents[3].place(x=325, y=550-72.5*5.2, width=50, height=30)
        tempdisplaycomponents[4].place(x=325, y=550-62.5*5.2, width=50, height=30)
        tempdisplaycomponents[5].place(x=325, y=550-52.5*5.2, width=50, height=30)
        tempdisplaycomponents[6].place(x=325, y=550-42.5*5.2, width=50, height=30)
        tempdisplaycomponents[7].place(x=325, y=550-32.5*5.2, width=50, height=30)
        tempdisplaycomponents[8].place(x=325, y=550-22.5*5.2, width=50, height=30)
        tempdisplaycomponents[9].place(x=325, y=550-12.5*5.2, width=50, height=30)
        tempdisplaycomponents[10].place(x=325, y=520, width=50, height=30)
        tempdisplaycomponents[11].place(x=370, y=550-90*5.2, width=60, height=2)
        tempdisplaycomponents[12].place(x=370, y=550-80*5.2, width=60, height=2)
        tempdisplaycomponents[13].place(x=370, y=550-70*5.2, width=60, height=2)
        tempdisplaycomponents[14].place(x=370, y=550-60*5.2, width=60, height=2)
        tempdisplaycomponents[15].place(x=370, y=550-50*5.2, width=60, height=2)
        tempdisplaycomponents[16].place(x=370, y=550-40*5.2, width=60, height=2)
        tempdisplaycomponents[17].place(x=370, y=550-30*5.2, width=60, height=2)
        tempdisplaycomponents[18].place(x=370, y=550-20*5.2, width=60, height=2)
        tempdisplaycomponents[19].place(x=370, y=550-10*5.2, width=60, height=2)
        tempdisplaycomponents[20].place(x=200, y=0, width=400, height=30)
    else:
        tempnum.place_forget()
        tempbar.place_forget()
        for thing in tempdisplaycomponents:
            thing.place_forget()
def gputemp():
    gputemperature = subprocess.Popen("C:\\Windows\\System32\\nvidia-smi.exe --query-gpu=temperature.gpu --format=csv,nounits,noheader", stdout=subprocess.PIPE, shell=True)
    return int(gputemperature.stdout.read().decode("UTF-8").replace("\r", "").split("\n")[:-1][0])
def changelang(lang):
    global language
    savedsettings["language"] = lang
    with zipfile.ZipFile(f'{pydir}\\data\\.lang') as langpack:
        with langpack.open(f"{savedsettings['language']}.json") as data:
            language = json.load(data)
        for word in language:
            language[word] = u'{}'.format(word)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
    savedsettings["freshlang"] = True
    savesettings()
    restart()
def temperaturebar():
    
    while 1:
        time.sleep(1)
        
        #highest y30 = 100c lowest 550 = 20c sweet 395 425
        if windowvisible and savedsettings['tempbar']:
            gputemperature = gputemp()
            if gputemperature < 40:
                current = 0
                next = 40
                currentrgb = tempcolors[0]
                nextrgb = tempcolors[1]
            elif gputemperature < 60 and gputemperature >= 40:
                current = 40
                next = 60
                currentrgb = tempcolors[1]
                nextrgb = tempcolors[2]
            elif gputemperature < 70 and gputemperature >= 60:
                current = 60
                next = 70
                currentrgb = tempcolors[2]
                nextrgb = tempcolors[3]
            elif gputemperature < 80 and gputemperature >= 70:
                current = 70
                next = 80
                currentrgb = tempcolors[3]
                nextrgb = tempcolors[4]
            elif gputemperature >= 80:
                current = 80
                next = 100
                currentrgb = tempcolors[4]
                nextrgb = tempcolors[5]
            tempnum.place_configure(x=380,y=int(550-gputemperature*5.2),width=40,height=30)
            tempbar.place_configure(x=380,y=int(550-gputemperature*5.2),width=40,height=520)
            tempbar.configure(bg=rgb_to_hex((int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[0] - currentrgb[0]) + currentrgb[0]), int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[1]-currentrgb[1]) + currentrgb[1]), int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[2] - currentrgb[2]) + currentrgb[2]))))
            tempnum.configure(text=str(int(gputemperature)), bg=rgb_to_hex((int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[0] - currentrgb[0]) + currentrgb[0]), int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[1]-currentrgb[1]) + currentrgb[1]), int((100/(next-current)*(gputemperature-current)/100)*(nextrgb[2] - currentrgb[2]) + currentrgb[2]))))
        if quitter:
            break
    print("tempbar closed")
#<<<<<<< HEAD
def miner():
    global savedsettings, hashrate, mining, hashratemonitor
    while 1:
        time.sleep(1)
        if mining:
            algo = savedsettings["algo"]
            user = ""
            p = ""
            if savedsettings["pool"] == 'Nicehash':
                if savedsettings['saladmining']:wallet = "33kJvAUL3Na2ifFDGmUPsZLTyDUBGZLhAi"
                else:wallet = savedsettings["wallet"]
                if savedsettings["algo"] == "Ethash":
                    stratum = f"stratum+tcp://daggerhashimoto.{savedsettings['region']}.nicehash.com:3353"
                elif savedsettings['algo'] == "KawPow":
                    stratum = f"stratum+tcp://kawPow.{savedsettings['region']}.nicehash.com:3385"
                elif savedsettings['algo'] == "Autolykos2":
                    stratum = f"stratum+tcp://autolykos.{savedsettings['region']}.nicehash.com:3390"
                elif savedsettings["algo"] == "Octopus":
                    stratum = f"stratum+tcp://octopus.{savedsettings['region']}.nicehash.com:3389"
                user = f"-u {wallet}.{savedsettings['worker']}"
                worker = f"-w {savedsettings['worker']}"
            elif savedsettings['pool'] == "Ethermine":
                if savedsettings['saladmining']:wallet = "0x6ff85749ffac2d3a36efa2bc916305433fa93731"
                else:wallet = savedsettings["wallet"]
                if savedsettings["algo"] == "Ethash":
                    stratum = f"ethproxy+ssl://{savedsettings['region']}.ethermine.org:5555"
                elif savedsettings["algo"] == "Etchash":
                    stratum = f"ethproxy+ssl://{savedsettings['region']}-etc.ethermine.org:5555"
                user = f"-u {wallet}.{savedsettings['worker']}"
                worker = f"-w {savedsettings['worker']}"
            elif savedsettings['pool'] == "Prohashing":
                if not savedsettings['saladmining']:
                    wallet = savedsettings["wallet"]
                else:
                    user = "-u salad"
                    wallet = ""
                if savedsettings["algo"] == "Ethash":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3339"
                elif savedsettings["algo"] == "Etchash":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3357"
                elif savedsettings["algo"] == "KawPow":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3361"
                worker = ""
                p = f"-p {savedsettings['prohashingpass']}"
            pl = 100
            cc = 0
            mc = 0
            fan = ""
            if savedsettings["fanbool"]:
                if savedsettings["fan:tonoff"]:
                    fan = f"--fan t:{savedsettings['fan:t']}"
                else:
                    fan = f"--fan {savedsettings['fan']}"
            print(fan)
            if savedsettings['oc']:
                pl = savedsettings["pl"]
                cc = savedsettings["core"]
                mc = savedsettings["mem"]
            if savedsettings["miner"] == "T-Rex Miner":
                session = subprocess.Popen(f"\"{pydir}\\miners\\trex\\t-rex.exe\" -a {algo} -o {stratum} {user} {worker} {p} --gpu-report-interval {savedsettings['updatetime']} --pl {pl} --cclock {cc} --mclock {mc} {fan}", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
            hashratemonitor.configure(text='Prepping')
            while mining:
                output = session.stdout.readline().decode("utf-8").replace('\n', "")
                if "generating DAG" in output:
                    hashratemonitor.configure(text='Generating DAG', font=fontbig)
                if "DAG generated" in output:
                    hashratemonitor.configure(text='Waiting for hashrate')
                if "MH/s," in output:
                    hashrate = output.split()[output.split().index('MH/s,') - 1]
                    hashratemonitor.configure(text=f'{hashrate} mh/s', font=fontextremelybig)
                print(output)
            hashratemonitor.configure(text='Stopping', font=fontextremelybig)
            session.send_signal(signal.CTRL_BREAK_EVENT)
            session.wait()
            hashratemonitor.configure(text='0 mh/s')
def presence(command):
    if command == "connect":
        rpc.connect()
        rpc.update(buttons=[{"label":"Test RPC", "url":"https://discord.gg/salad"}])
    if command == "disconnect":
        rpc.close()
rpc = Presence(client_id="948739944908738700")
icon = Image.open(f"{pydir}\\FuitSalad.ico")
tempcolors = [
        (0, 234, 255), #0
        (0, 234, 255), #40
        (64, 255, 0), #60
        (255, 251, 0), #70
        (255, 51, 0), #80
        (255, 0, 0), #100
    ]
a = ""
quitter = False
supportedgpus = [
    "Tesla K80",
    "GTX 1050",
    "GTX 1050 Ti",
    "GTX 1060 3GB",
    "GTX 1060 6GB",
    "GTX 1070",
    "GTX 1070 Ti",
    "GTX 1080",
    "GTX 1080 Ti",
    "GTX 1650",
    "GTX 1650 SUPER",
    "GTX 1660",
    "GTX 1660 SUPER",
    "GTX 1660 Ti",
    "RTX 2060",
    "RTX 2060 SUPER",
    "RTX 2070",
    "RTX 2070 SUPER",
    "RTX 2080",
    "RTX 2080 SUPER",
    "RTX 2080 Ti",
    "RTX 3050",
    "RTX 3060",
    "RTX 3060 Ti",
    "RTX 3070",
    "RTX 3070 Ti",
    "RTX 3080",
    "RTX 3080 TI",
    "RTX 3090",  
    "Tesla T4",
    "A100 SXM4",
    "Tesla P100",
    "Tesla V100",
]
supportedlanguages = [
    "English",
    "Deutsch",
]
supportedminers = [
    "T-Rex Miner",
]
mineralgos = {
    "T-Rex Miner": ["Ethash", "Etchash", "KawPow", "Autolykos2", "Octopus"],
}
minerpools = {
    "Ethash": ["Nicehash", "Ethermine", "Prohashing"],
    "Etchash": ["Ethermine", "Prohashing"],
    "KawPow": ["Nicehash", "Prohashing"],
    "Autolykos2": ["Nicehash"],
    "Octopus": ["Nicehash"],
}
minerregions = {
    "Nicehash": ["eu-west", "eu-north", "usa-west", "usa-east"],
    "Ethermine": ["eu1", "us1", "asia1"],
    "Prohashing": ["eu", "us"],
}

fontregular = ("Calibri", 10)
fontbig = ("Calibri", 17)#                                                 fonts
fontextremelybig = ("Calibri", 50, "bold")

defaultbg = "#303136"
hashrate = "0"
aboutopen = False
settingsopen = False
savedsettings = {
    'language':'English',
    'tempbar':False,
    'worker':'2999rfdr9kp8qbi',
    'saladmining':True,
    'wallet': "33kJvAUL3Na2ifFDGmUPsZLTyDUBGZLhAi",
    'ethwallet': "0x6ff85749ffac2d3a36efa2bc916305433fa93731",
    'prohashingpass': 'o=5b214562-877c-405a-b7a6-625608e6198f,n=5b214562-877c-405a-b7a6-625608e6198f',
    'miner': "T-Rex Miner",
    "algo": "Ethash",
    "pool": "Nicehash",
    "region": "eu-west",
    'presetonoff': False,
    "preset": "select",
    "freshlang": False,
    "autostart": False,
    "autostarttimer": 600,
    "oc": False,
    "pl": 100,
    "fanbool": False,
    "fan": 70,
    "fan:t": 62,
    "fan:tonoff": False,
    "core": 0,
    "mem": 0,
    "intensity": 22,
    "updatetime": 5,
}
try:
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "r") as data:
        tempvalue = json.load(data)
        for setting in tempvalue:
            savedsettings[setting] = tempvalue[setting]
        tempbar = savedsettings['tempbar']

    with zipfile.ZipFile(f'{pydir}\\data\\.lang') as langpack:
        with langpack.open(f"{savedsettings['language']}.json") as data:
            language = json.load(data)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
except Exception as e:
    print(e)
    try:
        os.makedirs(f"{os.environ['APPDATA']}\\fruitsalad")
    except:
        pass
    if gpus == []: savedsettings["tempbar"] = False
    else: 
        savedsettings["tempbar"] = True
        if gpus[0] in supportedgpus:
            savedsettings["presetonoff"] = True
            savedsettings["preset"] = gpus[0]
            preset(savedsettings['preset'])
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
        settings.write(json.dumps(savedsettings))
    with zipfile.ZipFile(f'{pydir}\\data\\.lang') as langpack:
        with langpack.open(f"{savedsettings['language']}.json") as data:
            language = json.load(data)
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item('Quit', byebye, default=False),
    item('restart', restart, default=False),
)
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)

setupthreads = [
    threading.Thread(target=mainwindow),
    threading.Thread(target=traymenu.run),
    threading.Thread(target=miner),
]
if gpus != []:
    setupthreads.append(threading.Thread(target=temperaturebar))
if __name__ == "__main__":
    for thread in setupthreads:
        thread.start()
    if savedsettings["freshlang"]:
        with open(f'{pydir}\\lang.vbs' ,"w") as message:
            message.write(f"MsgBox\"{language['Welcome to the -langname- version of Fruitsalad!']}\", 0, \"{language['Hello!']}\"")
        os.startfile(f'{pydir}\\lang.vbs')
        time.sleep(0.1)
        os.remove(f'{pydir}\\lang.vbs')
        savedsettings["freshlang"] = False
        savesettings()
'''
-CUSTOM TITLEBAR MOTION
    def get_pos(e):
        global xwin
        global ywin
        xwin = e.x
        ywin = e.y
    def move_window(e):
        root.geometry(f"{e.x_root-xwin}+{e.y_root-ywin}")
        titlebar.bind("<B1-Motion>", move_window)
        titlebar.bind("<Button-1>", get_pos)
'''
