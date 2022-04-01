import tkinter.colorchooser, tkinter.simpledialog, tkinter, tkinter.font, tkinter.ttk, time, winsound, json, requests
#print(tkinter.colorchooser.askcolor()[1])
print(json.loads(requests.get('https://api.github.com/repos/Letronix624/Fruit-Salad/releases').text)[0]['tag_name'])
