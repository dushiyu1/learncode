import requests
import base64
import json
import tkinter as tk
from tkinter import *
import tkinter.filedialog
from PIL import Image,ImageTk


def choosepic():
    path_ = tkinter.filedialog.askopenfilename()
    #获取图片路径
    path.set(path_)

def kasihishibie():
    client_id = "请输入自己的ID"
    client_secret = "请输入自己的密钥"
    lujing = path.get()
    #s.set(path.get())
    
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_id+'&'+'client_secret='+client_secret
    response = requests.get(host)
    if response:
        taken = response.json()

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license"

    f = open(lujing, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = taken['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    result = requests.post(request_url, data=params, headers=headers)

    if response:
        a = result.json()

        品牌型号 = a['words_result']['品牌型号']['words']
        发证日期 = a['words_result']['发证日期']['words']
        车辆类型 = a['words_result']['车辆类型']['words']
        所有人 = a['words_result']['所有人']['words']
        使用性质 = a['words_result']['使用性质']['words']
        发动机号码 = a['words_result']['发动机号码']['words']
        号牌号码 = a['words_result']['号牌号码']['words']
        注册日期 = a['words_result']['注册日期']['words']
        车辆识别代号 = a['words_result']['车辆识别代号']['words']

        s1.set("车牌号："+号牌号码)
        s2.set("车辆类型："+车辆类型)
        s3.set("所有人："+所有人)
        s4.set("使用性质："+使用性质)
        s5.set("品牌型号："+品牌型号)
        s6.set("车辆识别代号:"+车辆识别代号)
        s7.set("发动机号码:"+发动机号码)
        s8.set("注册日期:"+注册日期)
        s9.set("发证日期:"+发证日期)
               
root=Tk()
root.title("行驶证识别系统")
root.geometry('370x270') 
path=StringVar()



s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()
s7 = StringVar()
s8 = StringVar()
s9 = StringVar()


Button1=tk.Button(root,text='选择图片',command=choosepic)
Button1.pack()

e1=Entry(root,state='readonly',text=path,width=45)
e1.pack()


Button2=tk.Button(root,text='开始识别',command=kasihishibie)
Button2.pack()


e2=Entry(root,state='readonly',text=s1,width=45)
e2.pack()

e3=Entry(root,state='readonly',text=s2,width=45)
e3.pack()

e4=Entry(root,state='readonly',text=s3,width=45)
e4.pack()

e5=Entry(root,state='readonly',text=s4,width=45)
e5.pack()

e6=Entry(root,state='readonly',text=s5,width=45)
e6.pack()

e7=Entry(root,state='readonly',text=s6,width=45)
e7.pack()

e8=Entry(root,state='readonly',text=s7,width=45)
e8.pack()

e9=Entry(root,state='readonly',text=s8,width=45)
e9.pack()

e10=Entry(root,state='readonly',text=s9,width=45)
e10.pack()


root.mainloop()


