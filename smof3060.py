import signal
print(signal.valid_signals())
from PIL import ImageTk, Image
import time, win32api, threading, os, subprocess, json, tkinter
pydir = os.path.dirname(os.path.realpath(__file__))
root = tkinter.Tk()
root.title("Fruit Salad")
root.iconbitmap(f'{pydir}\\3060.ico')
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="orange")
root.mainloop()
os.system('title AFK Version of the Salad Miner Optimized For The 3060')
def cls(): os.system("cls")
last = time.time()
with open(f"{os.path.dirname(os.path.realpath(__file__))}" + r"\data\last.json", "r") as data:
    megaguide = json.load(data)
try:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}" + r"\data\config.txt", "r") as data:
        timer = int(data.read())
except:
    print("How many seconds do you have to be afk for the miner to start?")
    while 1:
        try:
            timer = int(input("Seconds: "))
            cls()
            with open(f"{os.path.dirname(os.path.realpath(__file__))}" + r"\data\config.txt", "w") as data:
                data.write(str(timer))
            break
        except Exception as ex:
            print(ex)
def updateinput():
    global last
    a = 0
    last = time.time()
    while True:
        if win32api.GetLastInputInfo() != a:
            a = win32api.GetLastInputInfo()
            last = time.time()
        time.sleep(1)
def miner():
    while 1:
        time.sleep(1)
        if last + timer < time.time():
            print(f"starting \"{os.path.dirname(os.path.realpath(__file__))}\\trex\\t-rex.exe\"")
            session = subprocess.Popen(f"\"{os.path.dirname(os.path.realpath(__file__))}\\trex\\t-rex.exe\" -a {megaguide['algo']} -o {megaguide['url']} -u {megaguide['user']}.{megaguide['worker']} -w {megaguide['worker']} {megaguide['3060']}", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            while last + timer < time.time():
                time.sleep(1)
            session.send_signal(signal.CTRL_BREAK_EVENT)
            session.wait()
            cls()
            print("Stopped mining")
            time.sleep(2)
            cls()
            print(f"If you want to change the times input your new time. Current: {str(timer)}")
if __name__ == "__main__":
    lastinput = threading.Thread(target=updateinput)
    mining = threading.Thread(target=miner)
    lastinput.start()
    mining.start()
    while 1:
        cls()
        print(f"If you want to change the times input your new time. Current: {str(timer)}")
        try:
            timer = int(input("new: "))
            with open(f"{os.path.dirname(os.path.realpath(__file__))}" + r"\data\config.txt", "w") as data:
                data.write(str(timer))
        except:
            print("You need to input a number.")
            input("---Press enter---")#(; purrfect