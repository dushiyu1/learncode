import tkinter as tk

win = tk.Tk()
win.title("my window")

def anniu():
    global a
    a.set(li.get(li.curselection()))

a = tk.StringVar()
label=tk.Label(win,bg="yellow",width=15,textvariable=a)
label.pack()

button = tk.Button(text="print selection",command=anniu)
button.pack()

var1 = tk.StringVar()
var1.set(["dushiyu","huangshuting","qiumingyue","xiangyumei"])
li = tk.Listbox(win,listvariable=var1)
li.insert(1,"11")
li.insert("end","22")
li.insert(2,"33")
li.delete(2)
items = ["4","5","6","7"]
for i in items:
    li.insert("end",i)

li.pack()

win.mainloop()