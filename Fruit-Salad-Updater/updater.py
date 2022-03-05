import os, zipfile, tkinter, time, requests, threading, shutil, sys
from win32api import GetSystemMetrics
def update():
    pydir = sys.executable[:-12]
    try:
        version = requests.get('http://seflon.ddns.net/secret/version.txt').text
    except:
        window.quit()
        os._exit(0)
    global display
    display.configure(text="Deleting old")
    for item in os.listdir():
        if not "updater" in item:
            print(f"removing {item}")
            try:
                os.remove(f"{pydir}\\{item}")
            except:
                shutil.rmtree(f"{pydir}\\{item}")
    display.configure(text="Downloading")
    #download
    filename = "hello.howareyou"
    with requests.get("http://seflon.ddns.net/secret/FruitSalad.zip", stream=True) as r:
        print('Downloading Package')
        r.raise_for_status()
        with open(f"{pydir}//{filename}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Package made")
    display.configure(text="Extracting")
    print(f"Extracting files to {pydir}")
    with zipfile.ZipFile(f"{pydir}\\{filename}", "r") as data:
        data.extractall(pydir)
    print(f'Downloaded Fruit Salad {version}')
    display.configure(text="Version "+version)
    os.remove(f"{pydir}\\{filename}")
    os.startfile(f"{pydir}\\FruitSalad.exe")
    time.sleep(1)
    os._exit(0)
window = tkinter.Tk()
window.geometry("400x100+"+str(GetSystemMetrics(0)/2-200)[:-2]+"+"+str(GetSystemMetrics(1)/2-50)[:-2])
window.overrideredirect(True)
window.resizable(False, False)
window.attributes('-topmost', True)
font = ("Miriam Libre", 35)
window.configure(background="#C4C4C4")
tkinter.Canvas(window, bg="#C4C4C4", highlightthickness=10, highlightbackground="black").place(x=2,y=2,width=396,height=96)
display = tkinter.Label(window, text="Starting", bg="#C4C4C4", font=font, fg="black")
display.place(x=12,y=12, width=400-24, height=100-24)
threading.Thread(target=update).start()
window.mainloop()