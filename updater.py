import os, zipfile, tkinter, time, requests, threading
from win32api import GetSystemMetrics
def update():
    global display
    time.sleep(1)
    display.configure(text="Downloading")
    time.sleep(1)
    display.configure(text="Extracting")
    time.sleep(1)
    display.configure(text="Finishing")
    time.sleep(1)
    window.quit()
window = tkinter.Tk()
window.geometry("400x100+"+str(GetSystemMetrics(0)/2-200)[:-2]+"+"+str(GetSystemMetrics(1)/2-50)[:-2])
window.overrideredirect(True)
window.resizable(False, False)
window.attributes('-topmost', True)
font = ("Miriam Libre", 40)
window.configure(background="#C4C4C4")
tkinter.Canvas(window, bg="#C4C4C4", highlightthickness=10, highlightbackground="black").place(x=2,y=2,width=396,height=96)
display = tkinter.Label(window, text="Starting", bg="#C4C4C4", font=font, fg="black")
display.place(x=12,y=12, width=400-24, height=100-24)
threading.Thread(target=update).start()
window.mainloop()