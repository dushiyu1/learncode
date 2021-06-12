from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在

root = Tk()
root.title('图片搜索小程序')
Label(root,text = '搜索文件夹：').grid(row = 0)
Label(root,text = '输出文件夹：').grid(row = 1)
e1 = Entry(root,width = 50)
e2 = Entry(root,width = 50)

e1.grid(row = 0, column = 1, padx = 10, pady = 10)
e2.grid(row = 1, column = 1, padx = 10, pady = 10)

def openfile():
    fileName = filedialog.askopenfilename()
    taget = e1.get()
    output = e2.get()
    print('选取样本：',fileName)
    print('搜索文件夹:',taget)
    print('输出文件夹:',output)
#    e1.delete(0,END)
#    e2.delete(0,END)
    

Button(root, text = '选取样本', width = 10, command = openfile)\
.grid(sticky = W, padx = 20, pady = 10)

#Button(root, text = '退出', width = 10, command = root.quit)\
#.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 5)

mainloop()