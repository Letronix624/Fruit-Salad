version = "0.3.4"
import sys
try:
    import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray, webbrowser, tkinter.messagebox, singleton, winsound, zipfile, win32gui, win32con, requests, winreg, tkinter.filedialog, shutil, random
    from tkinter import E, W, S, N, ttk
    from pypresence import Presence
    from PIL import ImageTk, Image
    from pystray import MenuItem as item
except ImportError: #import by HaveFUNRICH#0884
    print('''
    ❌ | Dependencies not found!
    🤖 | To fix this critical error, run 'pip install -r requirements.txt' or 'python -m pip install -r requirements.txt'
    ''')
    input()
    sys.exit()
if sys.version_info[0] < 3:
    print('''
    ❌ | Python 2 are not supported
    🤖 | To fix this critical error, download Python 3 (3.8 minimum)
    ''')
    input()
    sys.exit()
elif sys.version_info[1] < 10:
    print('''
    ❌ | Python 3.9 and under are not supported
    🤖 | Reason: You have farted in your life before.
    🤖 | To fix this error, download at least Python 3.10
    ''')
    input()
    sys.exit()
pydir = os.path.dirname(os.path.realpath(__file__))
exedir = sys.executable

try: #only one instance
    FruitSaladSession = singleton.SingleInstance()
except:#error message
    with open(f'{pydir}\\fail.vbs' ,"w") as message:
        message.write(f"MsgBox\"Hey there sadly you can only open Fruit Salad once\", 0, \"Epic Mining Fail!\"")
    os.startfile(f'{pydir}\\fail.vbs')
    time.sleep(0.1)
    os.remove(f'{pydir}\\fail.vbs')
    os._exit(0)
try:
    os.remove(f'{pydir}\\updater.exe')
except:pass
try:
    arg1 = sys.argv[1]
except:arg1 = ""
if sys.argv[0].endswith(".exe") and not "-console" in arg1:
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    try:
        if requests.get('http://seflon.ddns.net/secret/version.txt').text != version and not version.endswith("pre"):
            with requests.get('http://seflon.ddns.net/secret/updater.exe') as updaterbytes:
                updaterbytes.raise_for_status()
                print(pydir)
                with open(f"{pydir}\\updater.exe", 'wb') as f:
                    for chunk in updaterbytes.iter_content(chunk_size=8192):
                        f.write(chunk)
                time.sleep(0.1)
                os.startfile(f'{pydir}\\updater.exe')
                os._exit(0)
    except:print("website offline")
if "-forceupdate" in arg1:
    try:
        with requests.get('http://seflon.ddns.net/secret/updater.exe') as updaterbytes:
            updaterbytes.raise_for_status()
            print(pydir)
            with open(f"{pydir}\\updater.exe", 'wb') as f:
                for chunk in updaterbytes.iter_content(chunk_size=8192):
                    f.write(chunk)
            time.sleep(0.1)
            os.startfile(f'{pydir}\\updater.exe')
            os._exit(0)
    except:print("website offline")
try: #to get the name of the gpu
    gpunamerslkefjeslafjlska = subprocess.Popen(f"{os.environ['WINDIR']}\\System32\\nvidia-smi.exe --query-gpu=name --format=csv,nounits,noheader", stdout=subprocess.PIPE, shell=True)
    gpus = gpunamerslkefjeslafjlska.stdout.read().decode("UTF-8")[6:].replace("\r", "").replace(" GeForce ", "").split("\n")[:-1]
except: #no gpu
    gpus = []
del gpunamerslkefjeslafjlska
loglist = []
mining = False
class installminer():
    def __init__(self, miner):
        if miner == "trex":
            if not os.path.exists(f'{pydir}\\miners\\trex\\t-rex.exe'):
                try:
                    os.makedirs(f'{pydir}\\miners\\trex')
                except:print("path exists")
                minerGitAPI = json.loads(requests.get('https://api.github.com/repos/trexminer/T-Rex/releases').text)[0]['tag_name']#by HaveFUNRICH#0884
                hashratemonitor.configure(text=f'Downloading T-rex Miner', font=calibrimedium)
                with requests.get(f"https://github.com/trexminer/T-Rex/releases/download/{minerGitAPI}/t-rex-{minerGitAPI}-win.zip") as minerinstaller:
                    minerinstaller.raise_for_status()
                    with open(f"{pydir}\\miners\\trex\\extracting.zip", 'wb') as f:
                        for chunk in minerinstaller.iter_content(chunk_size=8192):
                            f.write(chunk)
                hashratemonitor.configure(text=f'Extracting T-rex Miner', font=calibrimedium)
                with zipfile.ZipFile(f"{pydir}\\miners\\trex\\extracting.zip", "r") as data:
                    data.extract("t-rex.exe", path=f'{pydir}\\miners\\trex')
                hashratemonitor.configure(text=f'Done', font=calibribold)
                os.remove(f"{pydir}\\miners\\trex\\extracting.zip")
                time.sleep(1)
        elif miner == "phoenix":
            if not os.path.exists(f'{pydir}\\miners\\phoenixminer\\PhoenixMiner.exe'):
                try:
                    os.makedirs(f'{pydir}\\miners\\phoenixminer')
                except:print("path exists")
                minerGitAPI = json.loads(requests.get('https://api.github.com/repos/spark-pool/PhoenixMiner/releases').text)[0]['tag_name']#by HaveFUNRICH#0884
                hashratemonitor.configure(text=f'Downloading Phoenix Miner', font=calibrimedium)
                with requests.get(f"https://github.com/spark-pool/PhoenixMiner/releases/download/{minerGitAPI}/PhoenixMiner_{minerGitAPI}_Windows.zip") as phoenix:
                    phoenix.raise_for_status()
                    with open(f"{pydir}\\miners\\phoenixminer\\extracting.zip", "wb") as f:
                        for chunk in phoenix.iter_content(chunk_size=8192):
                            f.write(chunk)
                hashratemonitor.configure(text=f'Extracting Phoenix Miner', font=calibrimedium)
                with zipfile.ZipFile(f"{pydir}\\miners\\phoenixminer\\extracting.zip", "r") as f:
                    f.extractall(f"{pydir}\\miners\\phoenixminer")
                os.remove(f"{pydir}\\miners\\phoenixminer\\extracting.zip")
                hi = os.listdir(f"{pydir}\\miners\\phoenixminer")[0]
                shutil.copyfile(f"{pydir}\\miners\\phoenixminer\\{hi}\\PhoenixMiner.exe", f"{pydir}\\miners\\phoenixminer\\PhoenixMiner.exe")
                shutil.rmtree(f"{pydir}\\miners\\phoenixminer\\{hi}")
                time.sleep(1)
        elif miner == "nb":
            if not os.path.exists(f'{pydir}\\miners\\nbminer\\nbminer.exe'):
                try:
                    os.makedirs(f'{pydir}\\miners\\nbminer')
                except:print("path exists")
                minerGitAPI = json.loads(requests.get('https://api.github.com/repos/NebuTech/NBMiner/releases').text)[0]['tag_name']#by HaveFUNRICH#0884
                hashratemonitor.configure(text=f'Downloading NBMiner', font=calibrimedium)
                with requests.get(f"https://github.com/NebuTech/NBMiner/releases/download/{minerGitAPI}/NBMiner_{minerGitAPI[1:]}_Win.zip") as minerinstaller:
                    minerinstaller.raise_for_status()
                    with open(f"{pydir}\\miners\\nbminer\\extracting.zip", "wb") as f:
                        for chunk in minerinstaller.iter_content(chunk_size=8192):
                            f.write(chunk)
                hashratemonitor.configure(text=f'Extracting NBMiner', font=calibrimedium)
                with zipfile.ZipFile(f"{pydir}\\miners\\nbminer\\extracting.zip", "r") as f:
                    f.extractall(f"{pydir}\\miners\\nbminer")
                os.remove(f"{pydir}\\miners\\nbminer\\extracting.zip")
                hi = os.listdir(f"{pydir}\\miners\\nbminer")[0]
                shutil.copyfile(f"{pydir}\\miners\\nbminer\\{hi}\\nbminer.exe", f"{pydir}\\miners\\nbminer\\nbminer.exe")
                shutil.rmtree(f"{pydir}\\miners\\nbminer\\{hi}")
                time.sleep(1)

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
def regadd():
    if sys.argv[0].endswith(".exe"):
        with open(f'{pydir}\\FruitSalad.bat', "w") as data:
            data.write(f'start "" "{sys.executable}"')
        openr=winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(openr,"FruitSalad",0,winreg.REG_SZ,f'"{pydir}\\FruitSalad.bat"')
        winreg.CloseKey(openr)
def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value
def mainwindow():
    global hashratemonitor, tempnum, startbuttonanimation, tempbar, root, windowvisible, startbutton, globalworker, globalminer, globalalgo, globalpool, globalregion, hashrate, calibriregular, calibrimedium, calibribold, tempdisplaycomponents, miningtext, FruitSalad, Discordbutton, starter
    global startbuttonstart, startbuttonstartani, startbuttonstop, startbuttonstopani, startbuttonload1, startbuttonload2, textcanvas, console, textframe, frame2
    windowvisible = True
    traymenu.update_menu()
    root = tkinter.Tk()
    root.configure(bg='#303136')
    with zipfile.ZipFile(f'{pydir}\\resources\\.gui') as getimages:
        with getimages.open('On Switch 1.png', 'r') as data:
            im1 = data.read()
        with getimages.open("Start Button.png", "r") as data:
            startbuttonstart = tkinter.PhotoImage(data=data.read(), format='png')
        with getimages.open("Start Button Animation.png", "r") as data:
            startbuttonstartani = tkinter.PhotoImage(data=data.read(), format='png')
        with getimages.open("Stop Button.png", "r") as data:
            startbuttonstop = tkinter.PhotoImage(data=data.read(), format='png')
        with getimages.open("Stop Button Animation.png", "r") as data:
            startbuttonstopani = tkinter.PhotoImage(data=data.read(), format='png')
        with getimages.open("Loading Button Animation1.png", "r") as data:
            startbuttonload1 = tkinter.PhotoImage(data=data.read(), format='png')
        with getimages.open("Loading Button Animation2.png", "r") as data:
            startbuttonload2 = tkinter.PhotoImage(data=data.read(), format='png')
            
        with getimages.open("FruitSalad.png", "r") as data:
            FruitSalad = ImageTk.PhotoImage(data=data.read(), format='png')
        with getimages.open("discord.png", "r") as data:
            Discordbutton = tkinter.PhotoImage(data=data.read(), format='png')
        startbuttonanimation = [
            ImageTk.PhotoImage(data=im1, format='png'),
        ]
    root.wm_attributes("-transparentcolor", '#010110')
    #Stats
    hashratemonitor = tkinter.Label(root, text=f'{hashrate} MH/s', bg='#303136', fg="white", font=calibribold)
    hashratemonitor.place(x=425, y=480, width=350, height=70)
    shift = 0
    for gpu in gpus:
        tkinter.Label(root, text=f"{language['GPU:'][:-1]+str(gpus.index(gpu))}: {gpu}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W).place(x=0, y=30+shift, width=400, height=50)
        shift = shift + 50
    globalminer = tkinter.Label(root, text=f"{language['Miner:']} {savedsettings['miner']}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W)
    globalminer.place(x=0, y=30+shift, width=400, height=50)
    globalalgo = tkinter.Label(root, text=f"{language['Algo:']} {savedsettings['algo']}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W)
    globalalgo.place(x=0, y=80+shift, width=400, height=50)
    globalpool = tkinter.Label(root, text=f"{language['Pool:']} {savedsettings['pool']}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W)
    globalpool.place(x=0, y=130+shift, width=400, height=50)
    globalworker = tkinter.Label(root, text=f"{language['Worker:']} {savedsettings['worker']}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W)
    globalworker.place(x=0, y=180+shift, width=400, height=50)
    globalregion = tkinter.Label(root, text=f"{language['Region:']} {savedsettings['region']}", bg='#303136', fg="white", font=calibrimedium, anchor=tkinter.W)
    globalregion.place(x=0, y=230+shift, width=400, height=50)
    #middle
    tkinter.Canvas(root, bg="#2D2C36", highlightthickness=0).place(x=375,y=30,width=50,height=520)#temptemptemptemp
    tempdisplaycomponents = [
        tkinter.Label(root, text='100°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='90°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='80°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='70°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='60°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='50°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='40°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='30°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='20°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='10°C', bg='#303136', fg="white", font=calibriregular),
        tkinter.Label(root, text='0°C', bg='#303136', fg="white", font=calibriregular),
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
    tempnum = tkinter.Label(root, bg="red", fg="white", font=calibriregular)
    #bottom
    tkinter.Canvas(root, bg="#0A2133", highlightthickness=0).place(x=0, y=550 ,width=800, height=50)
    startbutton = tkinter.Label(root,fg="white",bg="#0A2133", font=calibriregular, image=startbuttonanimation[0])
    startbutton.place(x=635,y=550,width=425,height=50)
    #top
    tkinter.Canvas(root, bg="#222129", highlightthickness=0).place(x=0,y=0,width=800,height=30)
    tkinter.Button(root, text=language['Settings'], bg='#222129', fg="white", border=1, font=calibriregular, command=opensettings).place(x=0, y=0, width=188, height=30)
    tempdisplaycomponents.append(tkinter.Label(root, text=language['GPU Temperature'], bg='#222129', fg="white", font=calibriregular))
    if savedsettings['tempbar']:
        tempdisplaycomponents[20].place(x=200, y=0, width=400, height=30)
    tkinter.Button(root, text=language['About us'], bg='#222129', fg="white", border=1, font=calibriregular, command=aboutus).place(x=612, y=0, width=188, height=30)
    #miningarea
    starter = tkinter.Button(root, image=startbuttonstart, bg=defaultbg, font=calibriregular, command=startminer, border=0, activebackground=defaultbg)
    starter.place(y=150, height=265, width=265, x=480)
    miningtext = tkinter.Label(root, text='Mining', font=calibrimedium, anchor=tkinter.W, background="black", foreground="yellow")
    miningtext.place(y=550, x=800, width=400, height=50)

    root.title("Fruit Salad "+ version)
    root.iconbitmap(f'{pydir}\\FruitSalad.ico')
    root.geometry("800x600")
    root.resizable(False, False)
    if savedsettings["ministart"]:
        root.withdraw()
        windowvisible = False
    else:
        root.lift()
        root.focus()
    root.protocol("WM_DELETE_WINDOW", windowclose)
    console = tkinter.Toplevel()
    console.withdraw()
    console.geometry("800x600")
    console.wm_minsize(400, 220)
    console.title(language["Console"])
    console.protocol("WM_DELETE_WINDOW", closeconsole)
    console.iconbitmap(f'{pydir}\\FruitSalad.ico')
    try:
        console.configure(bg=savedsettings["consolebg"])
        textframe = tkinter.Frame(console, background=savedsettings["consolebg"])
    except:
        console.configure(bg="black")
        textframe = tkinter.Frame(console, background="black")
        savedsettings["consolebg"] = "black"
    textframe.pack(fill=tkinter.BOTH, expand=1)
    textcanvas = tkinter.Canvas(textframe, bg=savedsettings["consolebg"], highlightthickness=0)
    textcanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    scrollbar = ttk.Scrollbar(textframe, orient=tkinter.VERTICAL, command=textcanvas.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    textcanvas.configure(yscrollcommand=scrollbar.set)
    textcanvas.bind("<Configure>", lambda e: textcanvas.configure(scrollregion=textcanvas.bbox("all")))
    frame2 = tkinter.Frame(textcanvas, bg=savedsettings["consolebg"])
    textcanvas.create_window((0,0), window=frame2, anchor=tkinter.NW)
    root.mainloop()
    print('root stopped')
def rgb_to_hex(rgb): return '#%02x%02x%02x' % rgb
def preset(thething):
    match thething:
        case "Tesla K80":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = False
        case "GTX 1050":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = -400
            savedsettings["mem"] = 550
            savedsettings["pl"] = 70
        case "GTX 1050 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
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
        case "GTX 1070 Ti":
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
        case "GTX 1080 Ti":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "Ethash"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 50
            savedsettings["mem"] = 500
            savedsettings["pl"] = 65
        case "GTX 1650":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
            savedsettings["pool"] = "Nicehash"
            savedsettings["oc"] = True
            savedsettings["core"] = 150
            savedsettings["mem"] = 700
            savedsettings["pl"] = 100
        case "GTX 1650 SUPER":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
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
        case "RTX 3050 Laptop GPU":
            savedsettings['miner'] = "T-Rex Miner"
            savedsettings['algo'] = "KawPow"
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
        case "RTX 3080 Ti":
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
    global aboutopen, FruitSalad
    def close():
        global aboutopen
        aboutopen = False
        about.destroy()
    def website(site):
        if site == 1:
            webbrowser.open("http://seflon.ddns.net/", new=2, autoraise=True)
        if site == 3:
            webbrowser.open('https://discord.gg/VUcgW3nqGM', new=2, autoraise=True)
    if not aboutopen:
        aboutopen = True
        about = tkinter.Toplevel()
        about.title(language["About us"])
        about.geometry("600x400")
        about.resizable(False, False)
        about.iconbitmap(f'{pydir}\\FruitSalad.ico')
        about.configure(bg='#303136')
        #About looks
        tkinter.Label(about, image=FruitSalad, background=defaultbg).place(x=6, y=6, width=64, height=64)
        tkinter.Label(about, text="Fruit Salad,", font=calibrimedium, bg='#303136', fg="white", anchor=tkinter.W).place(x=70, y=0)
        tkinter.Button(about, image=Discordbutton, bg=defaultbg, border=0, command=lambda: website(3), activebackground="#dabfdf").place(x=530, y=6, width=64, height=64)
        tkinter.Label(about, text=language["a Salad mining tool."], font=calibriregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=70, y=30)
        tkinter.Label(about, text=language["Made by Let Software"], font=calibriregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=70, y=50)
        tkinter.Button(about, text="seflon.ddns.net", font=calibriregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(1)).place(x=80, y=100)
        tkinter.Label(about, text="Let Software:", font=calibriregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y= 100)
        tkinter.Label(about, text="Letronix624#9040 (Let)", font=calibriregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 125)
        tkinter.Label(about, text="Nilsipilzi#9733 (brot)", font=calibriregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 145 )
        about.protocol("WM_DELETE_WINDOW", close)
    else:
        about.deiconify()
        about.focus()
def settingsclose():
    global settingsopen
    settingsopen = False
    settings.destroy()
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
        savedsettings["pl"] = int(pllot.get())
        savedsettings["core"] = int(cclot.get())
        savedsettings["mem"] = int(mclot.get())
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
        savedsettings["dcpresence"] = selectedpresence.get()
        savedsettings["ministart"] = selectedminimize.get()
        savedsettings["autostart"] = selectedautostart.get()
        savedsettings["devfee"] = selecteddevfee.get()
        savedsettings["consolebg"] = consolebg.get()
        savedsettings["consolefg"] = consolefg.get()
        savedsettings["consolefontsize"] = selectedconsolefontsize.get()
        try:
            console.configure(bg=savedsettings["consolebg"])
            textframe.configure(background=savedsettings["consolebg"])
            textcanvas.configure(background=savedsettings["consolebg"])
            frame2.configure(background=savedsettings["consolebg"])
            for item in loglist:
                item.configure(background=savedsettings["consolebg"], fg=savedsettings["consolefg"], font=(fontfamily, savedsettings["consolefontsize"]))
        except:
            console.configure(bg="black")
            textframe.configure(background="black")
            textcanvas.configure(background="black")
            frame2.configure(background="black")
            savedsettings["consolebg"] = "black"
            savedsettings["consolefg"] = "white"
            for item in loglist:
                item.configure(background=savedsettings["consolebg"], fg=savedsettings["consolefg"])
        if currentlyeditingmanual:
            savedsettings['worker'] = givenworker.get()
            prelabel.configure(text=savedsettings['worker'])
            globalworker.configure(text=f"{language['Worker:']} {savedsettings['worker']}")#PUPPER 666
        if editingwalleraddress:
            savedsettings['wallet'] = givenwallet.get()
            prolabel.configure(text=savedsettings["ethwallet"])
        if editingtime:
            savedsettings['autostarttimer'] = int(givenstarttime.get())
            presetshitfters[1].configure(text=str(savedsettings['autostarttimer']))
        if savedsettings['presetonoff']:
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
    def enableaccept(aseggsaegsdg = None): #$$$$$$$$$$$$$
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
        else:
            if selectedoc.get(): 
                state = "normal"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='lightgrey')
            else: 
                state = "disabled"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='grey')
        if not selectedcustomfan.get(): state = "disabled"
        else: state="normal"
        ocsettings2.configure(state=state)
        ocsettings4.configure(state=state)
        if selectedtempboundfanonoff.get(): 
            ocsettings5.configure(state="normal", troughcolor='lightgrey')
            ocsettings3.configure(state="disabled", troughcolor='grey')
        else:
            ocsettings5.configure(state="disabled", troughcolor='grey')
            ocsettings3.configure(state="normal", troughcolor='lightgrey')
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
        givenstarttime.place(x=210, y=130 + presetshift, width=35, height=24)
    def reset():
        PSYCHO_GROUPY_COCAIN_CRAZY = tkinter.messagebox.askokcancel(message=language["Are you sure you want to reset your settings?"], title="PSYCHO GROUPY COCAIN CRAZY", )
        if PSYCHO_GROUPY_COCAIN_CRAZY:
            os.remove(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json")
            restart()
    def profile(typea):
        if typea == "load":
            load = tkinter.filedialog.askopenfilename(title=language["Load settings profile"], filetypes=[("FruitSalad files", "*.let")])
        elif typea == "save":
            save = tkinter.filedialog.asksaveasfilename(title=language["Save settings profile"], filetypes=[("FruitSalad files", "*.let")])
        try:
            if load:
                temporarylanguage = savedsettings["language"]
                with open(load, "r") as data:
                    tempvalue = json.load(data)
                    for setting in tempvalue:
                        savedsettings[setting] = tempvalue[setting]
                    if temporarylanguage != savedsettings["language"]:
                        changelang(savedsettings["language"])
                    savesettings()
                    settingsclose()
        except:
            if save:
                if not save.endswith(".let"):
                    save = save + ".let"
                with open(save, "w") as data:
                    data.write(json.dumps(savedsettings))

    if not settingsopen:
        settingsopen = True
        settings = tkinter.Toplevel(bg=defaultbg)#PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY PSYCHO GROUPY COCAIN CRAZY
        settings.title(language["Settings"])
        settings.geometry("800x600")
        settings.resizable(False, False)
        settings.iconbitmap(f'{pydir}\\FruitSalad.ico')
        settings.protocol("WM_DELETE_WINDOW", settingsclose)
        settings.bind("<Return>", lambda event:settingchange())
        #nice cock ----- Layout ----- settings layout. Mining settings, app settings, advanced settings, SECRET SETTINGS\\\\\ CIGARO CIGARO CIGAR
        appsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        miningsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        advancedsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        megaguidesettingsframe = tkinter.Frame(settings, bg="pink")
        appsettingsframe.place(x=0, y=30, width=800, height=570)
        a = tkinter.Button(settings, text=language["App Settings"], font=calibriregular, bg='#46464A', fg="white", command=openappsettings, anchor=tkinter.S)
        a.place(x=0, y=0, width=300, height=40)
        b = tkinter.Button(settings, text=language["Mining Settings"], font=calibriregular, bg='#222129', fg="white", command=openminingsettings, anchor=tkinter.S)
        b.place(x=300, y=0, width=300, height=30)
        c = tkinter.Button(settings, text=language["Advanced Settings"], font=calibriregular, bg='#222129', fg="white", command=openadvancedsettings, anchor=tkinter.S)
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
        selectedpresence = tkinter.BooleanVar()
        selectedpresence.set(savedsettings["dcpresence"])
        selectedminimize = tkinter.BooleanVar()
        selectedminimize.set(savedsettings["ministart"])
        selecteddevfee = tkinter.IntVar()
        selecteddevfee.set(savedsettings["devfee"])
        
            #looks
        hhhh = tkinter.OptionMenu(appsettingsframe, selectedlang, *supportedlanguages, command=enableaccept)
        hhhh.place(x=5, y=13, width=100, height=24)
        hhhh.configure(highlightthickness=0)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Language. When applying program will restart."], anchor=tkinter.W).place(x=110, y=15, width=800, height=20)
        tempcheckbutton = tkinter.Checkbutton(appsettingsframe, onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg=defaultbg, variable=selectedtempbar, activebackground=defaultbg, fg="black")
        tempcheckbutton.place(x=5, y=45)
        tkinter.Checkbutton(appsettingsframe, onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg=defaultbg, variable=selectedpresence, activebackground=defaultbg, fg="black").place(x=5, y=75)
        tkinter.Checkbutton(appsettingsframe, onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg=defaultbg, variable=selectedminimize, activebackground=defaultbg, fg="black").place(x=5, y=105)
        tkinter.Scale(appsettingsframe, fg="white", background=defaultbg, highlightthickness=0, font=calibriregular, variable=selecteddevfee, from_=0, to=100, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept).place(x=5, y=135, width=240)
        if gpus == []:
            tempcheckbutton.configure(state="disabled")
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=f"{language['Temperature Bar']} | {language['When checked the temperature bar is visible.']}", anchor=tkinter.W).place(x=40, y=47, width=800, height=20)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=f"{language['Discord Presence | Show what you are mining and how long you mined for.']}", anchor=tkinter.W).place(x=40, y=77, width=800, height=20)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=f"{language['Start in tray | Minimizes the program on start.']}", anchor=tkinter.W).place(x=40, y=107, width=800, height=20)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=f"{language['Optional dev fee in % | Please support us.']}", anchor=tkinter.W).place(x=250, y=153, width=800, height=20)
        tkinter.Button(appsettingsframe, command=lambda: profile('save'), bg='white', fg="black", text=language["Save settings profile"]).place(y=183, x=5, height=30)
        tkinter.Button(appsettingsframe, command=lambda: profile('load'), bg='white', fg="black", text=language["Load settings profile"]).place(y=183, x=400, height=30)

        
        tkinter.Button(appsettingsframe, bg="red", text=language["RESET EVERYTHING"], command=reset).place(x=5, y=223, height=20)

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
        selectedautostart = tkinter.BooleanVar()
        selectedautostart.set(savedsettings["autostart"])

            #looks
        saladsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        nonsaladsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        presetoffsettings = tkinter.Frame(miningsettingsframe, bg=defaultbg)
        tkinter.Checkbutton(miningsettingsframe, text=language["Salad Mining?"], onvalue=True, offvalue=False, command=lambda:enableaccept("saladmining"), bg="#46464A", variable=selectedsaladmining, activebackground=defaultbg, fg="black").place(x=5, y=15, width=240)
        tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Should the miner mine to your Salad balance or an external wallet?"], anchor=tkinter.W).place(x=250, y=15, width=800, height=20)
        
            #salad
        prelabel = tkinter.Label(saladsettings, text=savedsettings['worker'], anchor=tkinter.W)
        manualworkergetterb = tkinter.Button(saladsettings, text=language['Manually set worker'],font=calibriregular, command=manualworkergetter)
        givenworker = tkinter.Entry(saladsettings)
        prelabel.place(x=10, y=45, height=20, width=100)
        tkinter.Button(saladsettings, text=language['Auto get worker'],font=calibriregular, command=autoworkergetter).place(x=120, y=45, height=20, width=180)
        manualworkergetterb.place(x=310, y=45, height=20, width=180)
        tkinter.Label(saladsettings, bg=defaultbg, fg="white", font=calibriregular, text=language['Worker to send the balance to.'], anchor=tkinter.W).place(x=500, y=45, width=800, height=20)
            #miner
        if savedsettings['saladmining']: saladsettings.place(x=0, y=0, width=800, height=570)
        else: nonsaladsettings.place(x=0, y=0, width=800, height=570)

        prolabel = tkinter.Label(nonsaladsettings, text=savedsettings['ethwallet'], anchor=tkinter.W)
        editwalletadress = tkinter.Button(nonsaladsettings, text=language['Edit'],font=calibriregular, command=changewalletaddress)
        givenwallet = tkinter.Entry(nonsaladsettings)
        prolabel.place(x=5, y=45, width=250, height=20)
        editwalletadress.place(x=260, y=45, width=60, height=20)
        tkinter.Label(nonsaladsettings, bg=defaultbg, fg="white", font=calibriregular, text=language['Wallet address'], anchor=tkinter.W).place(x=330, y=45, width=800, height=20)

        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=calibriregular, text=language['Miner:'][0:-1], anchor=tkinter.W).place(x=250, y=25, width=800, height=20)
        hhh = tkinter.OptionMenu(presetoffsettings, selectedminer, command=lambda x:enableaccept("minersettings"), *supportedminers) ##########################
        
        hhh.configure(highlightthickness=0)
        hhh.place(x=5, y=23, width=240, height=24)
        hhhha = tkinter.OptionMenu(presetoffsettings, selectedalgo, command=lambda x:enableaccept("minersettings"), *mineralgos[selectedminer.get()]) ###############################
        hhhha.configure(highlightthickness=0)
        hhhha.place(x=5, y=53, width=240, height=24)
        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=calibriregular, text=language['Algo:'][0:-1], anchor=tkinter.W).place(x=250, y=55, width=800, height=20)
        hhhaa = tkinter.OptionMenu(presetoffsettings, selectedpool, command=lambda x:enableaccept("minersettings"), *minerpools[selectedalgo.get()]) ###############################
        hhhaa.configure(highlightthickness=0)
        hhhaa.place(x=5, y=83, width=240, height=24)
        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=calibriregular, text=language['Pool:'][0:-1], anchor=tkinter.W).place(x=250, y=85, width=800, height=20)
        tkinter.Checkbutton(miningsettingsframe, text=language["Use preset"], onvalue=True, offvalue=False, command=lambda:enableaccept("preset"), bg="#46464A", variable=selectedpreset, activebackground=defaultbg, fg="black").place(x=5, y=70, width=240)
        #Use best settings premade for specified GPU.
        abcdefg = tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language['Use best settings premade for specified GPU.'], anchor=tkinter.W)
        if savedsettings['presetonoff']:
            abcdefg.place(y=70, x=410)
        else:
            abcdefg.place(y=70, x=250)
        h_haa = tkinter.OptionMenu(miningsettingsframe, selectedgpu, command=enableaccept, *supportedgpus)
        h_haa.configure(highlightthickness=0)
        if savedsettings['presetonoff']: h_haa.place(x=250, y=71, width=150, height=24)
        else: presetoffsettings.place(x=0, y=75, width=800, height=570)
        presetshitfters = [
            tkinter.Checkbutton(miningsettingsframe, text=language["Auto start"], onvalue=True, offvalue=False, variable=selectedautostart, command=lambda:enableaccept("p"), bg="#46464A", activebackground=defaultbg, fg="black"),
            tkinter.Label(miningsettingsframe, text=str(savedsettings['autostarttimer']), anchor=tkinter.W),
            tkinter.Button(miningsettingsframe, text=language['Edit'], command=changeautostarttime),
            tkinter.Button(miningsettingsframe, text=language['Scheduled mining settings'],font=calibriregular, command=openshedulemenu),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language['Autostart and how many seconds for it to start.'], anchor=tkinter.W),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language['Opens the settings to a schedule menu.'], anchor=tkinter.W),
            tkinter.OptionMenu(miningsettingsframe, selectedregion, command=lambda x:enableaccept("minersettings"), *minerregions[selectedpool.get()]),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language['Region:'][:-1], anchor=tkinter.W),
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
        selectedconsolefontsize = tkinter.IntVar()
        selectedconsolefontsize.set(savedsettings["consolefontsize"])
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
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language['Overclock GPU'] + " | " + language['Unlocks Overclock settings. (Know what you are doing!)'], anchor=tkinter.W).place(x=40, y=15, width=800, height=20)
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
        ocsettings0 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, state=ocstate, font=calibriregular, variable=selectedintensity, from_=8, to=25, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings0.place(x=5, y=125, width=240)
        ocsettings1 = tkinter.Checkbutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, variable=selectedcustomfan, onvalue=True, offvalue=False, command=lambda:enableaccept(''))
        ocsettings1.place(x=5, y=165)
        ocsettings2 = tkinter.Radiobutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, variable=selectedtempboundfanonoff, value=False, command=lambda:enableaccept(''))
        ocsettings2.place(x=5, y=195)
        ocsettings3 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, font=calibriregular, variable=selectedfixedfan, from_=0, to=100, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings3.place(x=5, y=215, width=240)
        ocsettings4 = tkinter.Radiobutton(advancedsettingsframe, background=defaultbg, activebackground=defaultbg, variable=selectedtempboundfanonoff, value=True, command=lambda:enableaccept(''))
        ocsettings4.place(x=5, y=257)
        ocsettings5 = tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, font=calibriregular, variable=selectedtempboundfan, from_=0, to=90, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept)
        ocsettings5.place(x=5, y=275, width=240)
        tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, highlightthickness=0, font=calibriregular, variable=selectedhashrateupdatetime, from_=5, to=60, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept).place(x=5, y=345, width=240)
        tkinter.Button(advancedsettingsframe, text=language['Open miner logs'], command=openconsole).place(x=5, y=390)
        consolebg = tkinter.Entry(advancedsettingsframe)
        consolebg.place(x=5, y=425, width=100, height=20)
        consolefg = tkinter.Entry(advancedsettingsframe)
        consolefg.place(x=5, y=455, width=100, height=20)
        consolebg.insert(tkinter.END, savedsettings['consolebg'])
        consolefg.insert(tkinter.END, savedsettings['consolefg'])
        tkinter.Scale(advancedsettingsframe, fg="white", background=defaultbg, variable=selectedconsolefontsize, highlightthickness=0, font=calibriregular, from_=1, to=50, orient=tkinter.HORIZONTAL, cursor='circle', command=enableaccept).place(x=5, y=480, width=240)




        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Power Limit"], anchor=tkinter.W).place(x=40, y=45, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Core Clock"], anchor=tkinter.W).place(x=40, y=75, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Memory Clock"], anchor=tkinter.W).place(x=40, y=105, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Intensity"], anchor=tkinter.W).place(x=250, y=142, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Custom fan speed"], anchor=tkinter.W).place(x=40, y=167, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Fixed fan speed"], anchor=tkinter.W).place(x=40, y=197, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Target fan speed in RPM"], anchor=tkinter.W).place(x=250, y=232, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Temp bound fan speed"], anchor=tkinter.W).place(x=40, y=260, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Target temperature in C"], anchor=tkinter.W).place(x=250, y=292, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Hashrate update frequency in seconds"], anchor=tkinter.W).place(x=250, y=362, width=800, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Logs window background color. # at beginning for hex code."], anchor=tkinter.W).place(x=110, y=425, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Logs window foreground color. # at beginning for hex code."], anchor=tkinter.W).place(x=110, y=455, height=20)
        tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text=language["Logs window font size"], anchor=tkinter.W).place(x=250, y=497, height=20)
        # preset tkinter.Label(advancedsettingsframe, bg=defaultbg, fg="white", font=calibriregular, text="", anchor=tkinter.W).place(x=250, y=0, height=20)
        #Megaguide Settings
        tkinter.Label(megaguidesettingsframe, text=language["Secret Settings"], bg="pink", fg="white", font=calibribold).pack()
        tkinter.Button(megaguidesettingsframe, text="Megaguide", bg="Red", fg="White", command=megaguide, font=calibriregular, padx=10, pady=5).pack(anchor=tkinter.NW)
        if savedsettings['language'] != "Furry":
            tkinter.Label(megaguidesettingsframe, text=language["Button below restarts the program."], font=calibriregular).pack(anchor=tkinter.NW)
            hhh = tkinter.Button(megaguidesettingsframe, text=language["Furry Language"], bg="yellow", fg="pink", font=calibriregular, command=lambda:changelang("Furry"))
            hhh.pack(anchor=tkinter.NW) #messageinblood
        #finishing touch
        if selectedpreset.get():
            pllot.configure(state="disabled")
            cclot.configure(state="disabled")
            mclot.configure(state="disabled")
            ocsettings0.configure(state="disabled", troughcolor='grey')
        else:
            if selectedoc.get(): 
                state = "normal"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='lightgrey')
            else: 
                state = "disabled"
                pllot.configure(state=state)
                cclot.configure(state=state)
                mclot.configure(state=state)
                ocsettings0.configure(state=state, troughcolor='grey')
        if not selectedcustomfan.get(): state = "disabled"
        else: state="normal"
        ocsettings2.configure(state=state)
        ocsettings4.configure(state=state)
        if selectedtempboundfanonoff.get(): 
            ocsettings5.configure(state="normal", troughcolor='lightgrey')
            ocsettings3.configure(state="disabled", troughcolor='grey')
        else:
            ocsettings5.configure(state="disabled", troughcolor='grey')
            ocsettings3.configure(state="normal", troughcolor='lightgrey')
    
    else:
        settings.deiconify()
        settings.focus()
def openshedulemenu(): #shedule shedule shedule shedule shedule shedule shedule shedule shedule shedule shedule shedule shedule shedule  
    global scheduleopen, shedulemenu, markerlist, selectedtime, selectedmarker, selectedprofile
    class createmarker:
        def __init__(self, xcoord=None, settings = 0, profile = "") -> None:
            global selectedmarker
            def die(x):
                self.canvas.destroy()
                titletext.configure(text=language["Create or select a marker."])
                unlockapply()
                deselectmarker()
            def select(s):
                global selectedtime, selectedmarker, selectedprofile
                starttime = str(time.strftime("%H:%M",time.gmtime(round((self.savedx/780) * 86400))))
                titletext.configure(text=language['Selected marker at {}.'].format(starttime))
                for object in markerlist:
                    try:
                        object.canvas.configure(bg="lightgray")
                    except:
                        del object
                self.canvas.configure(bg="yellow")
                selectedtime = round((self.savedx/780) * 86400)
                selectmarker(self.savedsetting, self.savedprofile)
                selectedmarker = self
            for object in markerlist:
                try:
                    object.canvas.configure(bg="lightgray")
                except:
                    del object
            if xcoord == None: 
                self.canvas = tkinter.Canvas(shedulemenu, bg="yellow")
                unlockapply()
                selectmarker(settings, profile)
                selectedmarker = self
            else:
                self.canvas = tkinter.Canvas(shedulemenu, bg="lightgrey")
                deselectall(1)
            self.savedx = globalx if xcoord == None else xcoord
            self.savedsetting = settings
            self.savedprofile = profile
            self.canvas.place(y=545, x=self.savedx+5, width=10, height=50)
            self.canvas.bind("<Button-3>", die)
            self.canvas.bind("<Button-1>", select)
    def close():
        global scheduleopen
        scheduleopen = False
        shedulemenu.destroy()
    def barclick(event):
        global globalx
        globalx = event.x
        starttime = str(time.strftime("%H:%M",time.gmtime(round((globalx/780) * 86400))))
        titletext.configure(text=language['Selected marker at {}.'].format(starttime))
        markerlist.append(createmarker())
    def deselectall(x):
        global markerlist, selectedmarker
        titletext.configure(text=language["Create or select a marker."])
        selectedmarker = None
        deselectmarker()
        for object in markerlist:
            try:
                object.canvas.configure(bg="lightgray")
            except:
                del markerlist[markerlist.index(object)]
    def unlockapply():
        applybutton.place(x=590,y=500, height=20, width=200)
        if selectedmarker: 
            selectedmarker.savedsetting = selection.get()
    def apply():
        deselectall(1)
        savedsettings["schedule"] = []
        for item in markerlist:
            savedsettings["schedule"].append([item.savedx, item.savedsetting, item.savedprofile])
        savedsettings["schedule"] = tuple(sorted(savedsettings["schedule"]))
        savesettings()
        applybutton.place_forget()
    def selectmarker(option, profile):
        global selectedprofile
        selection.set(option)
        selectedprofile = profile
        profilelabel.configure(text=f"{language['Directory:']} {selectedprofile}")
        startlabel.place(x=30, y=52, height=20)
        startchecker.place(x=5, y=50)
        stoplabel.place(x=30, y=82, height=20)
        stopchecker.place(x=5, y=80)
        switchprofilelabel.place(x=30, y=112, height=20)
        switchtoprofilechecker.place(x=5, y=110)
        profilebutton.place(x=10, y=142, height=20, width=150)
        profilelabel.place(x=160, y=142, height=20)
    def deselectmarker():
        startlabel.place_forget()
        startchecker.place_forget()
        stoplabel.place_forget()
        stopchecker.place_forget()
        switchprofilelabel.place_forget()
        switchtoprofilechecker.place_forget()
        profilebutton.place_forget()
        profilelabel.place_forget()
    def chooseprofile():
        currentprofile = tkinter.filedialog.askopenfilename(title=language["Load settings profile"], filetypes=[("FruitSalad files", "*.let")])
        if currentprofile:
            selectedprofile = currentprofile
            selectedmarker.savedprofile = selectedprofile
            profilelabel.configure(text=f"{language['Directory:']} {selectedprofile}")
            unlockapply()
            shedulemenu.focus()
    if scheduleopen:
        shedulemenu.deiconify()
        shedulemenu.focus()
    else:
        scheduleopen = True
        markerlist = []
        scheduletime = []
        selectionsettings = []
        profiledirectories = []
        for item in savedsettings["schedule"]:
            scheduletime.append(item[0])
            selectionsettings.append(item[1])
            profiledirectories.append(item[2])

        selection = tkinter.IntVar()
        selection.set(0)
        selectedmarker = None
        selectedtime = 0
        selectedprofile = ""
        shedulemenu = tkinter.Toplevel(bg=defaultbg)
        shedulemenu.title(language["Settings"])
        shedulemenu.geometry("800x600")
        shedulemenu.resizable(False, False)
        shedulemenu.iconbitmap(f'{pydir}\\FruitSalad.ico')
        shedulemenu.protocol("WM_DELETE_WINDOW", close)
        titletext = tkinter.Label(shedulemenu, bg=defaultbg, fg="white", font=calibrimedium, text=language["Create or select a marker."])
        titletext.place(x=10, y=10)
        tkinter.Canvas(shedulemenu, bg="#212126", highlightthickness=0).place(x=9, y=520, width=2, height=75)
        tkinter.Canvas(shedulemenu, bg="#212126", highlightthickness=0).place(x=204, y=520, width=2, height=75)
        tkinter.Canvas(shedulemenu, bg="#212126", highlightthickness=0).place(x=789, y=520, width=2, height=75)
        tkinter.Canvas(shedulemenu, bg="#212126", highlightthickness=0).place(x=399, y=520, width=2, height=75)
        tkinter.Canvas(shedulemenu, bg="#212126", highlightthickness=0).place(x=594, y=520, width=2, height=75)
        tkinter.Label(shedulemenu, bg=defaultbg, text="00:00", font=calibriregular, fg="white").place(x=11, y=520, height=30)
        tkinter.Label(shedulemenu, bg=defaultbg, text="06:00", font=calibriregular, fg="white").place(x=206, y=520, height=30)
        tkinter.Label(shedulemenu, bg=defaultbg, text="12:00", font=calibriregular, fg="white").place(x=401, y=520, height=30)
        tkinter.Label(shedulemenu, bg=defaultbg, text="18:00", font=calibriregular, fg="white").place(x=596, y=520, height=30)
        tkinter.Label(shedulemenu, bg=defaultbg, text="24:00", font=calibriregular, fg="white", anchor=E).place(x=708, y=520, height=30, width=80)
        startchecker = tkinter.Radiobutton(shedulemenu, variable=selection, value=1, command=unlockapply, bg=defaultbg, activebackground=defaultbg, fg="black")
        startlabel = tkinter.Label(shedulemenu, bg=defaultbg, fg="white", font=calibriregular, text=language["Start miner at that time."], anchor=tkinter.W)
        stopchecker = tkinter.Radiobutton(shedulemenu, variable=selection, value=2, command=unlockapply, bg=defaultbg, activebackground=defaultbg, fg="black")
        stoplabel = tkinter.Label(shedulemenu, bg=defaultbg, fg="white", font=calibriregular, text=language["Stop miner at that time."], anchor=tkinter.W)
        switchtoprofilechecker = tkinter.Radiobutton(shedulemenu, variable=selection, value=3, command=unlockapply, bg=defaultbg, activebackground=defaultbg, fg="black")
        switchprofilelabel = tkinter.Label(shedulemenu, bg=defaultbg, fg="white", font=calibriregular, text=language["Switch settings profile at that time."], anchor=tkinter.W)
        applybutton = tkinter.Button(shedulemenu, text=language["Accept Settings"], command=apply)
        profilebutton = tkinter.Button(shedulemenu, text=language["Change profile"], command=chooseprofile, font=calibriregular)
        profilelabel = tkinter.Label(shedulemenu, text=f"Directory: {selectedprofile}", background=defaultbg, font=calibriregular, fg="white")
        timebar = tkinter.Canvas(shedulemenu, bg="grey")
        timebar.place(x=10, y=550, height=40, width=780)
        for item in savedsettings["schedule"]:
            markerlist.append(createmarker(xcoord=item[0], settings=item[1], profile=item[2]))
        timebar.bind('<Button-1>',barclick)
        shedulemenu.bind('<Button-3>',deselectall)
def openconsole():
    global consoleopen
    console.wm_deiconify()
    consoleopen = True
def closeconsole():
    global consoleopen
    console.withdraw()
    consoleopen = False
consolelength = 0
def consoleadd(text):
    global consolelength
    if consoleopen:
        if consolelength > 1200:
            for item in range(int(round(len(loglist)/2)+10)):
                loglist[0].destroy()
                loglist.pop(0)
            consolelength = len(loglist)
        else:
            consolelength += 1
        try:
            loglist.append(tkinter.Label(frame2, text=text, bg=savedsettings["consolebg"], fg=savedsettings["consolefg"], font=(fontfamily, savedsettings["consolefontsize"])))
        except:
            loglist.append(tkinter.Label(frame2, text=text, bg="black", fg="white"), font=(fontfamily, savedsettings["consolefontsize"]))
        loglist[-1].pack(side=tkinter.TOP, anchor=tkinter.NW)
        textcanvas.configure(scrollregion=textcanvas.bbox("all"))
        textcanvas.yview_moveto('1.0')
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
            if savedsettings["dcpresence"] and kaboompshhhbadammkardosh:
                rpc.update(details="Currently not mining.", small_image="salad", small_text="Salad", buttons=[{"label": "Discord", "url": "https://discord.gg/VUcgW3nqGM"}])
            mining = False
            starter.configure(image=startbuttonstopani)
            for i in range(25):
                miningtext.place_configure(x=700+i*10)
                startbutton.place_configure(x=410+i*10)
                if i == 6:starter.configure(image=startbuttonload1)
                elif i == 12:starter.configure(image=startbuttonload2)
                time.sleep(0.01)
            starter.configure(image=startbuttonstart)
            stopminer()
        else:
            mining = True
            starter.configure(image=startbuttonstartani)
            for i in range(25):
                miningtext.place_configure(x=925+i*-10)
                startbutton.place_configure(x=635+i*-10)
                if i == 6:starter.configure(image=startbuttonload1)
                elif i == 12:starter.configure(image=startbuttonload2)
                time.sleep(0.01)
            starter.configure(image=startbuttonstop)
        done=True
    if done:
        threading.Thread(target=t).start()
def windowopen(hideshow):
    if hideshow:
        root.withdraw()
    else:
        root.deiconify()
def byebye(): #quit quit quit quit
    global quitter
    global windowvisible
    global mining
    global autostarttimer
    mining = False
    autostarttimer = 69420
    windowvisible = False
    root.withdraw()
    quitter = True
    traymenu.visible = False
    traymenu.stop()
    stopminer()
    os._exit(0)
def restart():
    global mining, autostarttimer
    autostarttimer = 69420
    mining = False
    traymenu.visible = False
    traymenu.stop()
    stopminer()
    os.startfile(sys.executable)
    os._exit(0)
def savesettings():
    stopminer()
    global tempdisplaycomponents
    if savedsettings['presetonoff']:
        preset(savedsettings["preset"])
    globalalgo.configure(text=f"{language['Algo:']} {savedsettings['algo']}")
    globalminer.configure(text=f"{language['Miner:']} {savedsettings['miner']}")
    globalpool.configure(text=f"{language['Pool:']} {savedsettings['pool']}")
    globalregion.configure(text=f"{language['Region:']} {savedsettings['region']}")
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
        print(savedsettings)
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
    with zipfile.ZipFile(f'{pydir}\\resources\\.lang') as langpack:
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
    global gputemperature
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
def stopminer():
    global mineractive, hashratemonitor, session
    if mineractive:
        hashratemonitor.configure(text='Stopping', font=calibribold)
        session.send_signal(signal.CTRL_BREAK_EVENT)
        session.wait()
        mineractive = False
        if currentminer == "nb":
            with subprocess.Popen(f"\"{pydir}\\miners\\nbminer\\nbminer.exe\" -a {savedsettings['algo'].lower()} -o stratum+tcp://daggerhashimoto.{savedsettings['region']}.nicehash.com:3353 -u {savedsettings['wallet']}.{savedsettings['worker']} --pl 100% --cclock 0 --mclock 0 --no-color", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE) as ocreset:
                time.sleep(3)
                ocreset.send_signal(signal.CTRL_BREAK_EVENT)
                ocreset.wait()
        hashratemonitor.configure(text='0.00 MH/s', font=calibribold)
        with open(f"{pydir}\\d.evs", "w") as data:
            data.write(str(devtimer))
def miner():
    global savedsettings, hashrate, mining, hashratemonitor, mineractive, session, devtimer, daggenerated, currentminer, sid
    while 1:
        time.sleep(1)
        if (mining or automining) and (devtimer > int(savedsettings["devfee"]) * 60):#==================================================
            algo = savedsettings["algo"]
            user = ""
            p = ""
            intensity = savedsettings["intensity"]
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
                elif savedsettings["algo"] == "Beamv3":
                    stratum = f"stratum+tcp://beamv3.{savedsettings['region']}.nicehash.com:3387"
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
            if savedsettings['oc']:
                pl = savedsettings["pl"]
                cc = savedsettings["core"]
                mc = savedsettings["mem"]
            if os.path.exists(f'{pydir}\\logs.txt'):
                os.remove(f'{pydir}\\logs.txt')
            try:
                session.send_signal(signal.CTRL_BREAK_EVENT)
                session.wait()
            except:pass
            if savedsettings["miner"] == "T-Rex Miner":
                installminer(miner='trex')
                session = subprocess.Popen(f"\"{pydir}\\miners\\trex\\t-rex.exe\" -a {algo} -o {stratum} {user} {worker} {p} --gpu-report-interval {savedsettings['updatetime']} --pl {pl} --cclock {cc} --mclock {mc} {fan} -i {savedsettings['intensity']} --autoupdate", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "trex"
            elif savedsettings["miner"] == "Phoenix Miner":
                installminer(miner="phoenix")
                if savedsettings["pool"] == "Nicehash":
                    stratum = stratum + " -proto 4 -stales 0"
                session = subprocess.Popen(f"\"{pydir}\\miners\\phoenixminer\\PhoenixMiner.exe\" -pool {stratum} {user.replace('-u ', '-wal ')} {p.replace('-p ', '-pass ')} {worker.replace('-w ', '-worker ')} -log 0 -rmode 0", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "pheonix"
            elif savedsettings["miner"] == "NBMiner":
                installminer(miner="nb")
                if savedsettings["fanbool"]:
                    fan = f"--fan {savedsettings['fan']}"
                session = subprocess.Popen(f"\"{pydir}\\miners\\nbminer\\nbminer.exe\" -a {algo.lower()} -o {stratum} {user} {p} --pl {pl}% --cclock {cc} --mclock {mc} -i {((int(intensity)-8)/17)*100} --no-color", shell=False, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "nb"

            
            daggenerated = False
            mineractive = True
            hashratemonitor.configure(text='Prepping', font=calibribold)
            while ((mining or automining) and mineractive) and devtimer > int(savedsettings["devfee"]) * 60:
                if currentminer == "nb":
                    time.sleep(int(savedsettings["updatetime"]))
                    nbminerapi = json.loads(requests.get("http://127.0.0.1:22333/api/v1/status").text)
                    
                    try:
                        hashrate = nbminerapi["miner"]["total_hashrate"][:-2]
                        hashratemonitor.configure(text=f'{hashrate} MH/s', font=calibribold)
                        if float(hashrate) > 0:daggenerated = True
                    except:
                        stopminer()
                else:
                    output = session.stdout.readline().decode("utf-8").replace('\n', "")
                    if output == "":stopminer()
                    if mineractive:
                        if "generating DAG" in output or "Building" in output:
                            hashratemonitor.configure(text='Generating DAG', font=calibrimedium)
                        if "DAG generated" in output or "Built" in output:
                            hashratemonitor.configure(text='Waiting for hashrate')
                            daggenerated = True
                        if "MH/s," in output:
                            if savedsettings["miner"] == "Phoenix Miner":hashrate = output.split()[output.split().index('MH/s,') - 1][:-1]
                            elif savedsettings["miner"] == "T-Rex Miner":hashrate = output.split()[output.split().index('MH/s,') - 1]
                            hashratemonitor.configure(text=f'{hashrate} MH/s', font=calibribold)
                    print(output)
                    consoleadd(output)
        if (mining or automining) and (devtimer < int(savedsettings["devfee"]) * 60):#======================================================================================
            algo = savedsettings["algo"]
            user = ""
            p = ""
            intensity = savedsettings["intensity"]
            if savedsettings["pool"] == 'Nicehash':
                if savedsettings["algo"] == "Ethash":
                    stratum = f"stratum+tcp://daggerhashimoto.{savedsettings['region']}.nicehash.com:3353"
                elif savedsettings['algo'] == "KawPow":
                    stratum = f"stratum+tcp://kawPow.{savedsettings['region']}.nicehash.com:3385"
                elif savedsettings['algo'] == "Autolykos2":
                    stratum = f"stratum+tcp://autolykos.{savedsettings['region']}.nicehash.com:3390"
                elif savedsettings["algo"] == "Octopus":
                    stratum = f"stratum+tcp://octopus.{savedsettings['region']}.nicehash.com:3389"
                elif savedsettings["algo"] == "Beamv3":
                    stratum = f"stratum+tcp://beamv3.{savedsettings['region']}.nicehash.com:3387"
                user = "-u 33kJvAUL3Na2ifFDGmUPsZLTyDUBGZLhAi.2999rfdr9kp8qbi"
                worker = "-w 2999rfdr9kp8qbi"
            elif savedsettings['pool'] == "Ethermine":
                if savedsettings["algo"] == "Ethash":
                    stratum = f"ethproxy+ssl://{savedsettings['region']}.ethermine.org:5555"
                elif savedsettings["algo"] == "Etchash":
                    stratum = f"ethproxy+ssl://{savedsettings['region']}-etc.ethermine.org:5555"
                user = "-u 0x6ff85749ffac2d3a36efa2bc916305433fa93731.2999rfdr9kp8qbi"
                worker = "-w 2999rfdr9kp8qbi"
            elif savedsettings['pool'] == "Prohashing":
                user = "-u salad"
                wallet = ""
                if savedsettings["algo"] == "Ethash":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3339"
                elif savedsettings["algo"] == "Etchash":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3357"
                elif savedsettings["algo"] == "KawPow":
                    stratum = f"stratum+tcp://{savedsettings['region']}.prohashing.com:3361"
                worker = ""
                p = "-p o=5b214562-877c-405a-b7a6-625608e6198f,n=5b214562-877c-405a-b7a6-625608e6198f"
            pl = 100
            cc = 0
            mc = 0
            fan = ""
            if savedsettings["fanbool"]:
                if savedsettings["fan:tonoff"]:
                    fan = f"--fan t:{savedsettings['fan:t']}"
                else:
                    fan = f"--fan {savedsettings['fan']}"
            if savedsettings['oc']:
                pl = savedsettings["pl"]
                cc = savedsettings["core"]
                mc = savedsettings["mem"]
            if os.path.exists(f'{pydir}\\logs.txt'):
                os.remove(f'{pydir}\\logs.txt')
            try:
                session.send_signal(signal.CTRL_BREAK_EVENT)
                session.wait()
            except:pass
            if savedsettings["miner"] == "T-Rex Miner":
                installminer(miner='trex')
                session = subprocess.Popen(f"\"{pydir}\\miners\\trex\\t-rex.exe\" -a {algo} -o {stratum} {user} {worker} {p} --gpu-report-interval {savedsettings['updatetime']} --pl {pl} --cclock {cc} --mclock {mc} {fan} -i {savedsettings['intensity']} --autoupdate", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "trex"
            elif savedsettings["miner"] == "Phoenix Miner":
                installminer(miner="phoenix")
                if savedsettings["pool"] == "Nicehash":
                    stratum = stratum + " -proto 4 -stales 0"
                session = subprocess.Popen(f"\"{pydir}\\miners\\phoenixminer\\PhoenixMiner.exe\" -pool {stratum} {user.replace('-u ', '-wal ')} {p.replace('-p ', '-pass ')} {worker.replace('-w ', '-worker ')} -log 0 -rmode 0", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "pheonix"
            elif savedsettings["miner"] == "NBMiner":
                installminer(miner="nb")
                if savedsettings["fanbool"]:
                    fan = f"--fan {savedsettings['fan']}"
                session = subprocess.Popen(f"\"{pydir}\\miners\\nbminer\\nbminer.exe\" -a {algo.lower()} -o {stratum} {user} {p} --pl {pl}% --cclock {cc} --mclock {mc} -i {((int(intensity)-8)/17)*100} --no-color", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE)
                currentminer = "nb"

            
            mineractive = True
            daggenerated = False
            hashratemonitor.configure(text='Prepping', font=calibribold)
            while ((mining or automining) and mineractive) and devtimer < int(savedsettings["devfee"]) * 60:
                if currentminer == "nb":
                    time.sleep(int(savedsettings["updatetime"]))
                    
                    try:
                        hashrate = json.loads(requests.get("http://127.0.0.1:22333/api/v1/status").text)["miner"]["total_hashrate"][:-2]
                        hashratemonitor.configure(text=f'{hashrate} MH/s', font=calibribold)
                        if float(hashrate) > 0:daggenerated = True
                    except:
                        stopminer()
                else:
                    output = session.stdout.readline().decode("utf-8").replace('\n', "")
                    if output == "":stopminer()
                    if mineractive:
                        if "generating DAG" in output or "Building" in output:
                            hashratemonitor.configure(text='Generating DAG', font=calibrimedium)
                        if "DAG generated" in output or "Built" in output:
                            hashratemonitor.configure(text='Waiting for hashrate')
                            daggenerated = True
                        if "MH/s," in output:
                            if savedsettings["miner"] == "Phoenix Miner":hashrate = output.split()[output.split().index('MH/s,') - 1][:-1]
                            elif savedsettings["miner"] == "T-Rex Miner":hashrate = output.split()[output.split().index('MH/s,') - 1]
                            hashratemonitor.configure(text=f'{hashrate} MH/s', font=calibribold)
                    print("dev: "+output)
                    consoleadd("dev: "+output)
def presence(command):
    global rpc
    if command == "connect":
        rpc.connect()
        rpc.update(instance=False, details="Currently not mining.", small_image="salad", small_text="Salad", buttons=[{"label": "Discord", "url": "https://discord.gg/VUcgW3nqGM"}])
    elif command == "disconnect":
        rpc.close()
icon = Image.open(f"{pydir}\\FruitSalad.ico")
sid = None
tempcolors = [
    (0, 234, 255), #0
    (0, 234, 255), #40
    (64, 255, 0), #60
    (255, 251, 0), #70
    (255, 51, 0), #80
    (255, 0, 0), #100
]
currentminer = ""
quitter = False
automining = False
consoleopen = False
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
    "RTX 3050 Laptop GPU",
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
    "Phoenix Miner",
    "NBMiner",
]
mineralgos = {
    "T-Rex Miner": ["Ethash", "Etchash", "KawPow", "Autolykos2", "Octopus"],
    "Phoenix Miner": ["Ethash", "Etchash"],
    "NBMiner": ["Ethash","Etchash", "KawPow", "Autolykos2", "Octopus", "Beamv3"]
}
minerpools = {
    "Ethash": ["Nicehash", "Ethermine", "Prohashing"],
    "Etchash": ["Ethermine", "Prohashing"],
    "KawPow": ["Nicehash", "Prohashing"],
    "Autolykos2": ["Nicehash"],
    "Octopus": ["Nicehash"],
    "Beamv3": ["Nicehash"],
}
minerregions = {
    "Nicehash": ["eu-west", "eu-north", "usa-west", "usa-east"],
    "Ethermine": ["eu1", "us1", "asia1"],
    "Prohashing": ["eu", "us"],
}

fontfamily = "Calibri"
calibriregular = (fontfamily, 10)
calibrimedium = (fontfamily, 17)#                                                 fonts
calibribold = (fontfamily, 50, "bold")

mineractive = False
defaultbg = "#303136"
hashrate = "0.00"
aboutopen = False
settingsopen = False
scheduleopen = False
savedsettings = {
    'language':'English',
    'tempbar':False,
    'worker':random.choice(seq=["2999rfdr9kp8qbi", "bskuc5ukd6hivho", "oflki151ra7dwxr"]),
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
    "dcpresence": False,
    "ministart":False,
    "devfee": 1,
    "schedule": [],
    "consolebg": "black",
    "consolefg": "white",
    "consolefontsize": 10,
}
try:
    with open(f"{pydir}\\d.evs", "r") as data:
       devtimer = int(data.read())
except:
    with open(f"{pydir}\\d.evs", "w") as data:
       devtimer = int(data.write("3"))
try:
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "r") as data:
        tempvalue = json.load(data)
        for setting in tempvalue:
            savedsettings[setting] = tempvalue[setting]
        tempbar = savedsettings['tempbar']

    with zipfile.ZipFile(f'{pydir}\\resources\\.lang') as langpack:
        with langpack.open(f"{savedsettings['language']}.json") as data:
            language = json.load(data)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
except Exception as e:
    print("Creating APPDATA folder")
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
    with zipfile.ZipFile(f'{pydir}\\resources\\.lang') as langpack:
        with langpack.open(f"{savedsettings['language']}.json") as data:
            language = json.load(data)
traymenucontent = (
    item('Show', lambda:windowopen(False), default=True, visible=False),
    item('Hide', lambda:windowopen(True), visible=True),
    item("Settings", opensettings),
    item("About Us", aboutus),
    item('Quit', byebye, default=False),
    item('restart', restart, default=False),
)
gputemperature = 0
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)
kaboom = True
daggenerated = False
autostarttimer = int(savedsettings["autostarttimer"])
rpcupdatecount = 15
lastinputid = 0
currentschedule = "disabled"
currentprofile = ""
possibleschedule = False
setupthreads = [
    threading.Thread(target=mainwindow),
    threading.Thread(target=traymenu.run),
    threading.Thread(target=miner),
]
kaboompshhhbadammkardosh = False
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
    if sys.executable.endswith(".exe"):
        regadd()
    while 1:
        time.sleep(1)
        if not kaboompshhhbadammkardosh:
            try:
                rpc = Presence(client_id="948739944908738700")
                kaboompshhhbadammkardosh = True
                print('Discord found')
            except:
                pass
        else:
            try:
                if savedsettings["dcpresence"] and kaboom:
                    kaboom = False
                    presence('connect')
                elif not savedsettings["dcpresence"] and not kaboom:
                    kaboom = True
                    presence("disconnect")
            except: 
                kaboompshhhbadammkardosh = False
                print("Discord lost")
        if mining or automining and daggenerated:
            devtimer -= 1
            if devtimer <= 0:
                devtimer = 6000
        rpcupdatecount += 1
        if (mining or automining) and (rpcupdatecount > 15) and kaboompshhhbadammkardosh:
            if savedsettings["algo"] == "Ethash":
                currencylogo = f"eth"
            elif savedsettings["algo"] == "Etchash":
                currencylogo = f"etc"
            elif savedsettings["algo"] == "KawPow":
                currencylogo = f"raven"
            elif savedsettings["algo"] == "Autolykos2":
                currencylogo = f"ergo"
            elif savedsettings["algo"] == "Octopus":
                currencylogo = f"octopus"
            if not windowvisible and savedsettings["tempbar"]:gputemperature = gputemp()
            if gpus[0]:
                details = f"Mining on a {gpus[0]}."
            if savedsettings["dcpresence"]:
                try:
                    rpc.update(instance=True, details=details, state=f"{str(gputemperature)}C, {str(int(round(float(hashrate.replace(',', '.')))))}MH/s", small_image=currencylogo, small_text=f"Mining {savedsettings['algo']}", buttons=[{"label": "Discord", "url": "https://discord.gg/VUcgW3nqGM"}], large_image="fruitsaladdark", large_text=f"Using {savedsettings['miner']}")
                    rpcupdatecount = 0
                except:pass
        if savedsettings["autostart"] and not mining:
            if win32api.GetLastInputInfo() != lastinputid:
                lastinputid = win32api.GetLastInputInfo()
                autostarttimer = int(savedsettings["autostarttimer"])
            if autostarttimer <= 0: automining = True
            else: 
                if mineractive:
                    if savedsettings["dcpresence"]:
                        rpc.update(details="Currently not mining.", small_image="salad", small_text="Salad")
                ####################
                stime = ((time.localtime()[3] * 60) + time.localtime()[4]) * 60 + time.localtime()[5]
                if savedsettings["schedule"] == () or savedsettings["schedule"] == []:
                    stopminer()
                    automining = False
                else:
                    for i in savedsettings["schedule"]:
                        if i[1]==1 or i[1]==2:possibleschedule=True
                        else:possibleschedule=False
                    if possibleschedule:
                        for i in savedsettings["schedule"]:
                            if ((i[0]/780) * 86400 > stime) or (i == savedsettings["schedule"][-1]):
                                if (i == savedsettings["schedule"][0]) or (stime > (round((savedsettings["schedule"][-1][0] / 780) * 86400))):
                                    if savedsettings["schedule"][-1][1] == 1:
                                        automining = True
                                    elif savedsettings["schedule"][-1][1] == 2:
                                        stopminer()
                                        automining = False
                                    elif savedsettings["schedule"][-1][1] == 3 and savedsettings["schedule"][-1][2] != "":
                                        if currentprofile != savedsettings["schedule"][-1][2]: 
                                            currentprofile = savedsettings["schedule"][-1][2]
                                            temporarylanguage = savedsettings["language"]
                                            with open(savedsettings["schedule"][-1][2], "r") as data:
                                                tempvalue = json.load(data)
                                                for setting in tempvalue:
                                                    if setting != "schedule":
                                                        savedsettings[setting] = tempvalue[setting]
                                                if temporarylanguage != savedsettings["language"]:
                                                    changelang(savedsettings["language"])
                                                savesettings()
                                                if settingsopen:
                                                    settingsclose()
                                else:
                                    if savedsettings["schedule"][savedsettings["schedule"].index(i)-1][1] == 1:
                                        automining = True
                                    elif savedsettings["schedule"][savedsettings["schedule"].index(i)-1][1] == 2:
                                        stopminer()
                                        automining = False
                                    elif savedsettings["schedule"][savedsettings["schedule"].index(i)-1][1] == 3 and savedsettings["schedule"][savedsettings["schedule"].index(i)-1][2] != "":
                                        if currentprofile != savedsettings["schedule"][savedsettings["schedule"].index(i)-1][2]:
                                            currentprofile = savedsettings["schedule"][savedsettings["schedule"].index(i)-1][2]
                                            temporarylanguage = savedsettings["language"]
                                            with open(savedsettings["schedule"][savedsettings["schedule"].index(i)-1][2], "r") as data:
                                                tempvalue = json.load(data)
                                                for setting in tempvalue:
                                                    if tempvalue[setting] != "schedule":
                                                        savedsettings[setting] = tempvalue[setting]
                                                if temporarylanguage != savedsettings["language"]:
                                                    changelang(savedsettings["language"])
                                                savesettings()
                                                if settingsopen:
                                                    settingsclose()
                                try:
                                    currentschedule = savedsettings["schedule"][savedsettings["schedule"].index(i)-1]
                                    break
                                except:break
                    else:
                        automining = False
                        stopminer()
                ####################
                autostarttimer -= 1

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