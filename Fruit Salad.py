import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray, GPUtil, webbrowser, clr, sys
pydir = os.path.dirname(os.path.realpath(__file__))
exedir = sys.executable
clr.AddReference(f'{pydir}\OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer
from PIL import ImageTk, Image
from pystray import MenuItem as item
from playsound import playsound
def mainwindow():
    global tempnum
    global startbuttonanimation
    global tempbar
    global root
    global windowvisible
    global startbutton
    windowvisible = True
    traymenu.update_menu()
    root = tkinter.Tk()
    root.configure(bg='#303136')
    startbuttonanimation = [
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 1.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 2.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 3.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 4.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 5.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 6.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 7.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 8.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 9.png"),
        ImageTk.PhotoImage(file=f"{pydir}\\GUI\\On Switch 10.png")
    ]
    root.wm_attributes("-transparentcolor", '#010110')
    #Stats
    tkinter.Label(root, text=f'{hashrate} mh/s', bg='#303136', fg="white", font=fontextremelybig).place(x=425, y=480, width=350, height=70)
    tkinter.Label(root, text=f"{language['GPU:']} {savedsettings['gpuname']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=30, width=400, height=50)
    tkinter.Label(root, text=language['Miner:'], bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=80, width=400, height=50)
    tkinter.Label(root, text=language['Algo:'], bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=130, width=400, height=50)
    tkinter.Label(root, text=language['Pool:'], bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=180, width=400, height=50)
    tkinter.Label(root, text=language['Region:'], bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=230, width=400, height=50)
    #middle
    tkinter.Label(root, text='100°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-100*5.2, width=50, height=30)
    tkinter.Label(root, text='90°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-92.5*5.2, width=50, height=30)
    tkinter.Label(root, text='80°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-82.5*5.2, width=50, height=30)
    tkinter.Label(root, text='70°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-72.5*5.2, width=50, height=30)
    tkinter.Label(root, text='60°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-62.5*5.2, width=50, height=30)
    tkinter.Label(root, text='50°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-52.5*5.2, width=50, height=30)
    tkinter.Label(root, text='40°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-42.5*5.2, width=50, height=30)
    tkinter.Label(root, text='30°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-32.5*5.2, width=50, height=30)
    tkinter.Label(root, text='20°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-22.5*5.2, width=50, height=30)
    tkinter.Label(root, text='10°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=550-12.5*5.2, width=50, height=30)
    tkinter.Label(root, text='0°C', bg='#303136', fg="white", font=fontregular).place(x=325, y=520, width=50, height=30)
    tkinter.Canvas(root, bg="#2D2C36", highlightthickness=0).place(x=375,y=30,width=50,height=520)#temptemptemptemp
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-90*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-80*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-70*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-60*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-50*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-40*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-30*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-20*5.2, width=60, height=2)
    tkinter.Canvas(root, bg='#212126', highlightthickness=0).place(x=370, y=550-10*5.2, width=60, height=2)
    tempbar = tkinter.Canvas(root, bg="red", highlightthickness=0)
    tempnum = tkinter.Label(root, bg="red", fg="white", font=fontregular)
    #bottom
    tkinter.Canvas(root, bg="#0A2133", highlightthickness=0).place(x=0, y=550 ,width=375, height=50)
    startbutton = tkinter.Button(root,fg="white",bg="#0A2133", border=0, font=fontregular, command=start, image=startbuttonanimation[1], activebackground="#0A2133")
    startbutton.place(x=375,y=550,width=425,height=50)
    tkinter.Button(root,fg="white", text=language['Auto start'],bg="red", border=2, font=fontregular).place(x=512,y=425,width=201,height=50)
    #top
    tkinter.Canvas(root, bg="#222129", highlightthickness=0).place(x=0,y=0,width=800,height=30)
    tkinter.Button(root, text=language['Settings'], bg='#222129', fg="white", border=1, font=fontregular, command=opensettings).place(x=0, y=0, width=188, height=30)
    tkinter.Label(root, text=language['GPU Temperature'], bg='#222129', fg="white", font=fontregular).place(x=200, y=0, width=400, height=30)
    tkinter.Button(root, text=language['About us'], bg='#222129', fg="white", border=1, font=fontregular, command=aboutus).place(x=612, y=0, width=188, height=30)


    root.title("Fruit Salad")
    root.iconbitmap(f'{pydir}\\3060.ico')
    root.geometry("800x600")
    root.resizable(False, False)
    


    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.protocol("WM_DELETE_WINDOW", windowclose)
    root.mainloop()
def trayicon():
    traymenu.run()
def rgb_to_hex(rgb): return '%02x%02x%02x' % rgb
def aboutus():
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
        about.iconbitmap(f'{pydir}\\3060.ico')
        about.configure(bg='#303136')
        #About looks
        tkinter.Label(about, text="Fruit Salad,", font=fontbig, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=0)
        tkinter.Label(about, text=language["a Salad mining manager."], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=10, y=30)
        tkinter.Label(about, text=language["Made by Let Software"], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=60)
        tkinter.Label(about, text=language["with help by Mezo#0001 from MezoMGMT"], font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y=100)
        tkinter.Button(about, text="seflon.ddns.net", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(1)).place(x=450, y=60)
        tkinter.Label(about, text="Let Software:", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=5, y= 140)
        tkinter.Label(about, text="Letronix624#9040 (Let)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 160)
        tkinter.Label(about, text="Nilsipilzi#9733 (brot)", font=fontregular, bg='#303136', fg="white", anchor=tkinter.W).place(x=15, y= 180)
        tkinter.Button(about, text="mezomgmt.com", font=fontregular, bg='#4B4C54', fg="orange", anchor=tkinter.W, border=0, command= lambda: website(2)).place(x=450, y=100)
        about.protocol("WM_DELETE_WINDOW", close)
    else:
        about.deiconify()
        about.focus()
def opensettings():#settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings - settings
    global settings
    global settingsopen
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
    def openminingsettings():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        miningsettingsframe.place(x=0, y=30, width=800, height=570)
    def openadvancedsettings():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        advancedsettingsframe.place(x=0, y=30, width=800, height=570)
    def openmegaguide():
        miningsettingsframe.place_forget()
        advancedsettingsframe.place_forget()
        appsettingsframe.place_forget()
        megaguidesettingsframe.place_forget()
        megaguidesettingsframe.place(x=0, y=30, width=800, height=570)
    def kickjesusfromchat():
        changelang("Furry")
        hhh.destroy()
    def settingchange():
        changelang(selectedlang.get())
        savedsettings["tempbar"] = selectedtempbar.get()
        savesettings()
        acceptbutton.place_forget()
    def enableaccept(aseggsaegsdg):
        acceptbutton.place(x=595, y=565, width=200, height=30)
    if not settingsopen:
        settingsopen = True
        settings = tkinter.Toplevel(bg=defaultbg)
        settings.title(language["Settings"])
        settings.geometry("800x600")
        settings.resizable(False, False)
        settings.iconbitmap(f'{pydir}\\3060.ico')
        settings.protocol("WM_DELETE_WINDOW", close)
        #nice cock ----- Layout ----- settings layout. Mining settings, app settings, advanced settings, SECRET SETTINGS
        appsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        miningsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        advancedsettingsframe = tkinter.Frame(settings, bg=defaultbg)
        megaguidesettingsframe = tkinter.Frame(settings, bg="pink")
        appsettingsframe.place(x=0, y=30, width=800, height=570)
        tkinter.Button(settings, text=language["App Settings"], font=fontregular, bg='#222129', fg="white", command=openappsettings).place(x=0, y=0, width=300, height=30)
        tkinter.Button(settings, text=language["Mining Settings"], font=fontregular, bg='#222129', fg="white", command=openminingsettings).place(x=300, y=0, width=300, height=30)
        tkinter.Button(settings, text=language["Advanced Settings"], font=fontregular, bg='#222129', fg="white", command=openadvancedsettings).place(x=600, y=0, width=200, height=30)
        tkinter.Button(settings, border=0, bg=defaultbg, command=openmegaguide).place(x=790, y=590, width=10, height=10)
        acceptbutton = tkinter.Button(settings, text=language['Accept Settings'], command=settingchange)


        #App Settings
        selectedlang = tkinter.StringVar()
        selectedlang.set(savedsettings['language'])
        selectedtempbar =tkinter.BooleanVar()
        selectedtempbar.set(savedsettings['tempbar'])
        hhhh = tkinter.OptionMenu(appsettingsframe, selectedlang, *supportedlanguages, command=enableaccept)
        hhhh.place(x=5, y=3, width=100, height=24)
        hhhh.configure(highlightthickness=0)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Language. Apply by closing the program in task manager and reopening."], anchor=tkinter.W).place(x=150, y=5, width=800, height=20)
        tempcheckbutton = tkinter.Checkbutton(appsettingsframe, text=language["Temperature Bar"], onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg=defaultbg, variable=selectedtempbar, activebackground=defaultbg, fg="black")
        tempcheckbutton.place(x=5, y=35)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["When checked the temperature bar is visible."], anchor=tkinter.W).place(x=150, y=35, width=800, height=20)

        #Mining Settings


        #Advanced Settings


        #Megaguide Settings
        tkinter.Label(megaguidesettingsframe, text=language["Secret Settings"], bg="pink", fg="white", font=fontextremelybig).pack()
        tkinter.Button(megaguidesettingsframe, text="Megaguide", bg="Red", fg="White", command=megaguide, font=fontregular, padx=10, pady=5).pack(anchor=tkinter.NW)
        if savedsettings['language'] != "Furry":
            tkinter.Label(megaguidesettingsframe, text=language["Button below requires Task Manager Restart."], font=fontregular).pack(anchor=tkinter.NW)
            hhh = tkinter.Button(megaguidesettingsframe, text=language["Furry Language"], bg="yellow", fg="pink", font=fontregular, command=kickjesusfromchat)
            hhh.pack(anchor=tkinter.NW) #messageinblood
        

        
    else:
        settings.deiconify()
        settings.focus()
def megaguide():
    def mega():
        playsound(f"{pydir}\\MEGAGUIDE.mp3")
    threading.Thread(target=mega).start()
def windowclose():
    global windowvisible
    windowvisible = False
    root.withdraw()
def start():
    def realclick():
        global mining
        global startbuttonanimation
        if mining:
            mining = False
            startbutton.configure(image=startbuttonanimation[8])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[7])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[6])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[5])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[4])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[3])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[2])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[1])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[0])
            time.sleep(0.05)
        else:
            mining = True
            startbutton.configure(image=startbuttonanimation[1])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[2])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[3])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[4])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[5])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[6])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[7])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[8])
            time.sleep(0.05)
            startbutton.configure(image=startbuttonanimation[9])
            time.sleep(0.05)
    threading.Thread(target=realclick).start()
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
def changesettings():
    savedsettings['gpuname'] = nvidia.get()
    savedsettings['language'] = defaultlang.get()
    savedsettings['tempbar'] = tempbar
    changelang(savedsettings['language'])
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
                settings.write(json.dumps(savedsettings))
    gpudefine.destroy()
def savesettings():
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
                settings.write(json.dumps(savedsettings))
    if savedsettings["tempbar"]:
        gputemperature = gputemp()
        tempnum.place(x=380,y=int(550-gputemperature*5.2),width=40,height=30)
        tempbar.place(x=380,y=int(550-gputemperature*5.2),width=40,height=520)
    else:
        tempnum.place_forget()
        tempbar.place_forget()
def gputemp():
    for a in range(0, len(c.Hardware[0].Sensors)):
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            temp = c.Hardware[0].Sensors[a].get_Value()
            c.Hardware[0].Update()
            return temp
def changelang(lang):
    global language
    savedsettings["language"] = lang
    with open(f"{pydir}\\languages\\{lang}.json") as data:
        language = json.load(data)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
    threading.Thread(target=mainwindow)
icon = Image.open(f"{pydir}\\3060.ico")
mining = False
fontregular = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 10, "bold")
fontbig = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 20, "bold")
fontextremelybig = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 50, "bold")
a = ""
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
supportedlanguages = [
    "English",
    "Deutsch",
]
defaultbg = "#303136"
hashrate = 0
aboutopen = False
settingsopen = False
savedsettings = {'gpuname':'', 'language':'', 'tempbar': True}
gpus = GPUtil.getGPUs()
c = Computer()
c.GPUEnabled = True
c.Open()
try:
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "r") as data:
        savedsettings = json.load(data)
        tempbar = savedsettings['tempbar']
        changelang(savedsettings["language"])
except Exception as e:
    print(e)
    try:
        os.makedirs(f"{os.environ['APPDATA']}\\fruitsalad")
    except:
        pass
    savedsettings["language"] = "English"
    savedsettings['gpuname'] = "Unknown"
    gpudefine = tkinter.Tk()
    tempbar = True
    nvidia = tkinter.StringVar()
    nvidia.set("Nvidia")
    defaultlang = tkinter.StringVar()
    defaultlang.set("English")
    tkinter.Label(gpudefine, text='Startup settings.', bg='#303136', fg="white", font=fontregular).pack()
    tkinter.Label(gpudefine, text="What gpu do you use.").pack()
    tkinter.OptionMenu(gpudefine, nvidia, *supportedgpus).pack()
    tkinter.Label(gpudefine, text="Language.").pack()
    tkinter.OptionMenu(gpudefine, defaultlang, *supportedlanguages).pack()
    tkinter.Button(gpudefine, text="Done", command=changesettings).pack()

    gpudefine.title("Fruit Salad")
    gpudefine.iconbitmap(f'{pydir}\\3060.ico')
    gpudefine.geometry("600x400")
    gpudefine.resizable(False, False)
    gpudefine.configure(bg='#303136')
    gpudefine.mainloop()
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item(language['Hide'], windowclose, default=False),
    #item('Quit', byebye, default=False)
)
if savedsettings["gpuname"] == "Unknown":
    savedsettings["gpuname"] == language["Unknown"]
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)



if __name__ == "__main__":
    traythread = threading.Thread(target=trayicon)
    traythread.start()
    threading.Thread(target=mainwindow).start()
    time.sleep(1)
    while 1:
        time.sleep(1)
        #highest y30 = 100c lowest 550 = 20c sweet 395 425
        if windowvisible and savedsettings['tempbar']:
            gputemperature = gputemp()
            tempnum.place_configure(x=380,y=int(550-gputemperature*5.2),width=40,height=30)
            tempbar.place_configure(x=380,y=int(550-gputemperature*5.2),width=40,height=520)
            tempnum.configure(text=str(int(gputemperature)))
        