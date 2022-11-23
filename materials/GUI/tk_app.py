from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
bar = ttk.Progressbar(frm, orient = HORIZONTAL)
bar.grid(column=0, row=0)

def increment(*args):
    print(args)
    if bar["value"] == 100:
        bar["value"] = 0
    else:
        bar["value"] += 20

button = ttk.Button(frm, text="INCREMENT", command=increment)
button.grid(column=1, row=0)

if __name__ == '__main__':
    root.mainloop()