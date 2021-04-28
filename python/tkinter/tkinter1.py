import tkinter as tk

root = tk.Tk()
root.title("my window")
root.geometry("400x200")

var = tk.StringVar()

label = tk.Label(root,textvariable=var,bg="green",font=("Arial",12),width=15)
label.pack()

enter = tk.Entry(root,show="❤️")
enter.pack()

text = tk.Text(root,height=2)
text.pack()

def dianji1():
    e = enter.get()
    text.insert("insert",e)

def dianji2():
    e = enter.get()
    text.insert("end",e)

button1 = tk.Button(root,text="在鼠标处插入",font=("Arial",12),width=15,command = dianji1)
button1.pack()

button2 = tk.Button(root,text="在尾部插入",font=("Arial",12),width=15,command = dianji2)
button2.pack()

on_hit = False

def dianji():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("hhhhhhh")
    else:
        on_hit = False
        var.set("")

button = tk.Button(root,text="hit me",font=("Arial",12),width=15,command=dianji)
button.pack()


root.mainloop()