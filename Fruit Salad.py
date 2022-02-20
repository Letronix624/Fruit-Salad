version = "0.0.0"
import time, win32api, threading, os, subprocess, json, tkinter, signal, pystray, webbrowser, sys, tkinter.messagebox, singleton
pydir = os.path.dirname(os.path.realpath(__file__))
exedir = sys.executable
try:
    FruitSaladSession = singleton.SingleInstance()
except:
    time.sleep(2)
    try:
        FruitSaladSession = singleton.SingleInstance()
    except:
        os.startfile(f"{pydir}\\fail.vbs")
        os._exit(0)
from PIL import ImageTk, Image
from pystray import MenuItem as item
from playsound import playsound
try:
    gpunamerslkefjeslafjlska = subprocess.Popen("C:\\Windows\\System32\\nvidia-smi.exe --query-gpu=name --format=csv,nounits,noheader", stdout=subprocess.PIPE, shell=True)
    gpus = gpunamerslkefjeslafjlska.stdout.read().decode("UTF-8")[15:].replace("\r", "").split("\n")[:-1]
except:
    gpus = ""
del gpunamerslkefjeslafjlska

mining = False
def mainwindow():
    global tempnum
    global startbuttonanimation
    global tempbar
    global root
    global windowvisible
    global startbutton
    global globalworker
    global globalminer
    global globalalgo
    global globalpool
    global s
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
    if gpus != []:
        tkinter.Label(root, text=f"{language['GPU:']} {gpus[0]}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W).place(x=0, y=30, width=400, height=50)
        shift = 0
    else:
        shift = -50
    globalminer = tkinter.Label(root, text=f"{language['Miner:']} {savedsettings['miner']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalminer.place(x=0, y=80+shift, width=400, height=50)
    globalalgo = tkinter.Label(root, text=f"{language['Algo:']} {savedsettings['algo']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalalgo.place(x=0, y=130+shift, width=400, height=50)
    globalpool = tkinter.Label(root, text=f"{language['Pool:']} {savedsettings['pool']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalpool.place(x=0, y=180+shift, width=400, height=50)
    globalworker = tkinter.Label(root, text=f"{language['Worker:']} {savedsettings['worker']}", bg='#303136', fg="white", font=fontbig, anchor=tkinter.W)
    globalworker.place(x=0, y=230+shift, width=400, height=50)
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
    s = threading.Thread(target=startminer)
    startbutton = tkinter.Button(root,fg="white",bg="#0A2133", border=0, font=fontregular, command=lambda: s.start(), image=startbuttonanimation[1], activebackground="#0A2133")
    startbutton.place(x=375,y=550,width=425,height=50)
    tkinter.Button(root,fg="white", text=language['Auto start'],bg="red", border=2, font=fontregular).place(x=430,y=35,width=182,height=50)
    tkinter.Button(root,fg="white", text=language['Auto start'],bg="red", border=2, font=fontregular).place(x=615,y=35,width=182,height=50)
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
    root.focus()
    root.protocol("WM_DELETE_WINDOW", windowclose)
    root.mainloop()
    print('root stopped')
def rgb_to_hex(rgb): return '#%02x%02x%02x' % rgb
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
    global currentlyeditingmanual
    currentlyeditingmanual = False
    editingwalleraddress = False
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
    def settingchange():
        global currentlyeditingmanual
        global editingwalleraddress
        savedsettings["tempbar"] = selectedtempbar.get()
        if currentlyeditingmanual:
            savedsettings['worker'] = givenworker.get()
            prelabel.configure(text=savedsettings['worker'])
            globalworker.configure(text=f"{language['Worker:']} {savedsettings['worker']}")
        if editingwalleraddress:
            savedsettings['ethwallet'] = givenwallet.get()
            prolabel.configure(text=savedsettings["ethwallet"])
        currentlyeditingmanual = False
        editingwalleraddress = False
        acceptbutton.place_forget()
        givenworker.place_forget()
        givenwallet.place_forget()
        manualworkergetterb.configure(state="normal")
        editwalletadress.configure(state="normal")
        savedsettings['miner'] = selectedminer.get()
        savedsettings['algo'] = selectedalgo.get()
        savedsettings["pool"] = selectedpool.get()
        savedsettings["presetonoff"] = selectedpreset.get()
        savedsettings["preset"] = selectedgpu.get()
        globalalgo.configure(text=f"{language['Algo:']} {savedsettings['algo']}")
        globalminer.configure(text=f"{language['Miner:']} {savedsettings['miner']}")
        globalpool.configure(text=f"{language['Pool:']} {savedsettings['pool']}")
        prelabel.place(x=10, y=45, height=20, width=100)
        prolabel.place(x=5, y=45, width=250, height=20)
        savedsettings['saladmining'] = selectedsaladmining.get()
        if selectedlang.get() != savedsettings["language"]:
            changelang(selectedlang.get())
        savesettings()
    def enableaccept(aseggsaegsdg):
        acceptbutton.place(x=595, y=565, width=200, height=30)
        if aseggsaegsdg == "saladmining":
            if selectedsaladmining.get():
                saladsettings.place(x=0, y=0, width=800, height=570)
                nonsaladsettings.place_forget()
            else:
                saladsettings.place_forget()
                nonsaladsettings.place(x=0, y=0, width=800, height=570)
        if aseggsaegsdg == "preset":
            if selectedpreset.get():
                h_haa.place(x=250, y=70, width=150, height=24)
                presetoffsettings.place_forget()
                presetshift = 0
                presetshitfters[0].place_configure(x=5, y=100 + presetshift, width=200)
                presetshitfters[1].place_configure(x=210, y=100 + presetshift, width=60)
                presetshitfters[2].place_configure(x=5, y=130 + presetshift, height=20, width=240)
                presetshitfters[3].place_configure(x=280, y=100 + presetshift, width=800, height=20)
                presetshitfters[4].place_configure(x=250, y=130 + presetshift, width=800, height=20)
                abcdefg.place_configure(y=70, x=410)
            else:
                h_haa.place_forget()
                presetoffsettings.place(x=0, y=75, width=800, height=570)
                presetshift = 90
                presetshitfters[0].place_configure(x=5, y=100 + presetshift, width=200)
                presetshitfters[1].place_configure(x=210, y=100 + presetshift, width=60)
                presetshitfters[2].place_configure(x=5, y=130 + presetshift, height=20, width=240)
                presetshitfters[3].place_configure(x=280, y=100 + presetshift, width=800, height=20)
                presetshitfters[4].place_configure(x=250, y=130 + presetshift, width=800, height=20)
                abcdefg.place_configure(y=70, x=250)
    def autoworkergetter():
        global currentlyeditingmanual
        currentlyeditingmanual = False
        givenworker.place_forget()
        prelabel.place(x=10, y=45, height=20, width=100)
        manualworkergetterb.configure(state="normal")
        try:
            with open(f"{os.environ['appdata']}\\Salad\\logs\\main.log","r")as data:
                for line in data:
                    if 'worker ID:' in line:
                        savedsettings['worker'] = line[21:-1]
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
    if not settingsopen:
        settingsopen = True
        settings = tkinter.Toplevel(bg=defaultbg)
        settings.title(language["Settings"])
        settings.geometry("800x600")
        settings.resizable(False, False)
        settings.iconbitmap(f'{pydir}\\3060.ico')
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
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["Language. When applying program will restart."], anchor=tkinter.W).place(x=150, y=10, width=800, height=20)
        tempcheckbutton = tkinter.Checkbutton(appsettingsframe, text=language["Temperature Bar"], onvalue=True, offvalue=False, command=lambda:enableaccept(1), bg="#46464A", variable=selectedtempbar, activebackground=defaultbg, fg="black")
        tempcheckbutton.place(x=5, y=45)
        tkinter.Label(appsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language["When checked the temperature bar is visible."], anchor=tkinter.W).place(x=150, y=45, width=800, height=20)
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
        hhh = tkinter.OptionMenu(presetoffsettings, selectedminer, command=enableaccept, *supportedminers)
        hhh.configure(highlightthickness=0)
        hhh.place(x=5, y=23, width=240, height=24)
        hhhha = tkinter.OptionMenu(presetoffsettings, selectedalgo, command=enableaccept, *mineralgos[selectedminer.get()])
        hhhha.configure(highlightthickness=0)
        hhhha.place(x=5, y=53, width=240, height=24)
        tkinter.Label(presetoffsettings, bg=defaultbg, fg="white", font=fontregular, text=language['Algo:'][0:-1], anchor=tkinter.W).place(x=250, y=55, width=800, height=20)
        hhhaa = tkinter.OptionMenu(presetoffsettings, selectedpool, command=enableaccept, *minerpools[selectedminer.get()])
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
            tkinter.Checkbutton(miningsettingsframe, text=language["Auto start"][:-1], onvalue=True, offvalue=False, command=lambda:enableaccept("p"), bg="#46464A", activebackground=defaultbg, fg="black"),
            tkinter.Button(miningsettingsframe, text=language['Edit']),
            tkinter.Button(miningsettingsframe, text=language['Scheduled mining settings'],font=fontregular),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Autostart and how many seconds for it to start.'], anchor=tkinter.W),
            tkinter.Label(miningsettingsframe, bg=defaultbg, fg="white", font=fontregular, text=language['Opens the settings to a schedule menu.'], anchor=tkinter.W),
        ]
        presetshitfters[0].place(x=5, y=100 + presetshift, width=200)
        presetshitfters[1].place(x=210, y=100 + presetshift, width=60)
        presetshitfters[2].place(x=5, y=130 + presetshift, height=20, width=240)
        presetshitfters[3].place(x=280, y=100 + presetshift, width=800, height=20)
        presetshitfters[4].place(x=250, y=130 + presetshift, width=800, height=20)
        #Advanced Settings


        #Megaguide Settings
        tkinter.Label(megaguidesettingsframe, text=language["Secret Settings"], bg="pink", fg="white", font=fontextremelybig).pack()
        tkinter.Button(megaguidesettingsframe, text="Megaguide", bg="Red", fg="White", command=megaguide, font=fontregular, padx=10, pady=5).pack(anchor=tkinter.NW)
        if savedsettings['language'] != "Furry":
            tkinter.Label(megaguidesettingsframe, text=language["Button below restarts the program."], font=fontregular).pack(anchor=tkinter.NW)
            hhh = tkinter.Button(megaguidesettingsframe, text=language["Furry Language"], bg="yellow", fg="pink", font=fontregular, command=kickjesusfromchat)
            hhh.pack(anchor=tkinter.NW) #messageinblood
        

        
    else:
        settings.deiconify()
        settings.focus()
def megaguide():
    playsound(f"{pydir}\\MEGAGUIDE.mp3", False)
def windowclose():
    global windowvisible
    windowvisible = False
    root.withdraw()
def startminer():
    global mining
    global s
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
        del s
        s = threading.Thread(target=startminer)
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
        del s
        s = threading.Thread(target=startminer)
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
def reset():
    os.remove(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json")
    os.startfile(sys.executable)
    traymenu.visible = False
    os._exit(0)
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
    gputemperature = subprocess.Popen("C:\\Windows\\System32\\nvidia-smi.exe --query-gpu=temperature.gpu --format=csv,nounits,noheader", stdout=subprocess.PIPE, shell=True)
    return int(gputemperature.stdout.read().decode("UTF-8").replace("\r", "").split("\n")[:-1][0])
def changelang(lang):
    global language
    savedsettings["language"] = lang
    with open(f"{pydir}\\languages\\{lang}.json") as data:
        language = json.load(data)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
    savedsettings["freshlang"] = True
    savesettings()
    os.startfile(sys.executable)
    traymenu.visible = False
    os._exit(0)
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
icon = Image.open(f"{pydir}\\3060.ico")
tempcolors = [
        (0, 234, 255), #0
        (0, 234, 255), #40
        (64, 255, 0), #60
        (255, 251, 0), #70
        (255, 51, 0), #80
        (255, 0, 0), #100
    ]
fontregular = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 10, "bold")
fontbig = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 17, "bold")
fontextremelybig = (f"{pydir}\\GUI\\BarlowCondensed-Medium.ttf", 50, "bold")
a = ""
quitter = False
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
supportedminers = [
    "T-Rex Miner",
]
mineralgos = {
    "T-Rex Miner": ["Ethash", "Etchash", "Kawpow", "Autolykos2", "Octopus"],
}
minerpools = {
    "T-Rex Miner": ["Nicehash", "Ethermine", "Prohashing"],
}
defaultbg = "#303136"
hashrate = 0
aboutopen = False
settingsopen = False
savedsettings = {'language':'', 'tempbar':True,'worker':'', 'saladmining':True, 'wallet': "", "algo": "", "pool": "", 'presetonoff': False, "preset": "", "freshlang": False}
try:
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "r") as data:
        savedsettings = json.load(data)
        tempbar = savedsettings['tempbar']
    with open(f"{pydir}\\languages\\{(savedsettings['language'])}.json") as data:
        language = json.load(data)
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", "w") as settings:
        settings.write(json.dumps(savedsettings))
except Exception as e:
    print(e)
    try:
        os.makedirs(f"{os.environ['APPDATA']}\\fruitsalad")
    except:
        pass
    savedsettings = {'language':'English', 'tempbar':True,'worker':'2999rfdr9kp8qbi', 'saladmining':True, 'nicehashwallet': "33kJvAUL3Na2ifFDGmUPsZLTyDUBGZLhAi", 'ethwallet': "0x6ff85749ffac2d3a36efa2bc916305433fa93731", 'miner': "T-Rex Miner", "algo": "Ethash", "pool": "Nicehash", 'presetonoff': False, "preset": "RTX 3060", "freshlang": False}
    if gpus[0] in supportedgpus:
        savedsettings["presetonoff"] = True
        savedsettings["preset"] = gpus[0]
    with open(f"{os.environ['APPDATA']}\\fruitsalad\\settings.json", ("w")) as settings:
        settings.write(json.dumps(savedsettings))
    with open(f"{pydir}\\languages\\{savedsettings['language']}.json") as data:
        language = json.load(data)
traymenucontent = (
    item('Show or hide', windowopen, default=True, visible=False),
    item('Quit', byebye, default=False)
)
traymenu = pystray.Icon("Fruit Salad", icon, "Fruit Salad", traymenucontent)
setupthreads = [
    threading.Thread(target=mainwindow),
    threading.Thread(target=temperaturebar),
    threading.Thread(target=traymenu.run)
]

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