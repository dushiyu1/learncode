import tkinter as tk
window = tk.Tk()
window.title("身份证管理系统")
window.geometry("400x400")

can = tk.Canvas(window,width=250,height=150)
image = tk.PhotoImage(file=r"/Users/toshigyoku/Downloads/gitcode/python/shenfenzheng/guoqi.png")
can.create_image(28,0,image=image,anchor="nw")
can.pack(side="top")

label1 = tk.Label(window,text="中华人民共和国居民身份信息管理系统",font=("",20))
label1.pack()

label2 = tk.Label(window,text="身份证号：",font=("",15))
label2.place(x = 100,y = 160 )

var1 = tk.StringVar()
entry = tk.Entry()
entry.place(x=120,y=160)


window.mainloop()