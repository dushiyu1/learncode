import tkinter as tk

win = tk.Tk()
win.title("my window")

var = tk.StringVar()
label = tk.Label(bg="yellow",width=20,textvariable=var)
label.pack()

def danxuan():
    var.set("you have selected" + var.get())
    

a1 = tk.Radiobutton(text="Option A",variable=var,value="A",command=danxuan)
a1.pack()

a2 = tk.Radiobutton(text="Option B",variable=var,value="B",command=danxuan)
a2.pack()

a3 = tk.Radiobutton(text="Option C",variable=var,value="C",command=danxuan)
a3.pack()



win.mainloop()