import tkinter as tk
win = tk.Tk()
win.title("阳光保险单证管理系统")
win.geometry("400x200")

var1 = tk.StringVar()
label1 = tk.Label(text="欢迎使用阳光保险单证管理系统")

label1.pack()

lin1 = tk.Entry()
lin1.pack()


def denglu():
    var1.set("欢迎使用单证管理系统")

btn1 = tk.Button(text="登陆",command=denglu)
btn1.pack()

win.mainloop()