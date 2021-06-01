import sys
import time
import random

from PyQt5.QtWidgets import (QDialog,QApplication,QLabel,QPushButton,
                             QFileDialog,QMessageBox,QPlainTextEdit,QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
import qdarkstyle
from PyQt5 import QtGui

import requests
import base64
import json
#头文件配置信息
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Gz8YooMGDOGdBCgz9GEmQN3Z&client_secret=XHD7noXfQdmeyxYsWUPQbnvVBFOVCLTo'
#host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6epPHS8EPX1k8GjdCzez7OLT&client_secret=onZaVAlgYzEBchooR91xQf8j7kgoFG4W'
response = requests.get(host)
if response:
    taken = response.json()
    #print(taken)
    #print(taken['access_token'])

'''
行驶证识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license"
# 二进制方式打开图片文件
f = open(r'/Users/toshigyoku/Downloads/222.JPG', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = taken['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
result = requests.post(request_url, data=params, headers=headers)

if response:
    a = result.json()
    # print (a) 以json字典格式打印数据

    品牌型号 = a['words_result']['品牌型号']['words']
    发证日期 = a['words_result']['发证日期']['words']
    车辆类型 = a['words_result']['车辆类型']['words']
    所有人 = a['words_result']['所有人']['words']
    使用性质 = a['words_result']['使用性质']['words']
    发动机号码 = a['words_result']['发动机号码']['words']
    号牌号码 = a['words_result']['号牌号码']['words']
    注册日期 = a['words_result']['注册日期']['words']
    车辆识别代号 = a['words_result']['车辆识别代号']['words']

    #print("号牌号码："+号牌号码)

class CarCardRecognize(QDialog):
    def __init__(self):
        super(CarCardRecognize,self).__init__()
        self.text = ""
        self.strTime = ""
        self.carid = ""
        self.filePath = ""
        self.initUI()

    def initUI(self):
        self.resize(700,600)
        self.setWindowTitle("行驶证信息识别系统")
        self.setWindowIcon(QIcon("./images/Icon.png"))

        self.plabel = QLabel(self)
        self.plabel.setFixedSize(400,300)

        self.obtn = QPushButton(self)
        self.obtn.setText("打开本地图片")
        self.obtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.obtn.clicked.connect(self.openimage)
        self.obtn.setFixedSize(180,40)
        self.sbtn = QPushButton(self)
        self.sbtn.setText("开 始 识 别")
        self.sbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.sbtn.clicked.connect(self.recognize)
        self.sbtn.setFixedSize(180,40)

        self.v1box = QVBoxLayout()
        self.v1box.addWidget(self.obtn)
        self.v1box.addWidget(self.sbtn)

        self.h1box = QHBoxLayout()
        self.h1box.addWidget(self.plabel)
        self.h1box.addLayout(self.v1box)

        self.tlabel = QLabel(self)
        self.tlabel.setText("识\n别\n结\n果")
        self.tlabel.setFont(QFont("苏新诗柳楷繁", 15))
        self.tlabel.resize(200, 50)

        self.tedit = QPlainTextEdit(self)
        self.tedit.setFont(QFont("宋体",25))
        self.tedit.setFixedSize(600,350)

        self.h2box = QHBoxLayout()
        self.h2box.addStretch(1)
        self.h2box.addWidget(self.tlabel)
        self.h2box.addStretch(1)
        self.h2box.addWidget(self.tedit)
        self.h2box.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.h1box)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.h2box)
        self.setLayout(self.vbox)


    def openimage(self):
        self.filePath, imgType = QFileDialog.getOpenFileName(self, "打开本地图片", "", "*.jpg;;*.png;;All Files(*)")
        self.jpg = QtGui.QPixmap(self.filePath).scaled(self.plabel.width(), self.plabel.height())
        self.plabel.setPixmap(self.jpg)

    def recognize(self):
        if(self.filePath == ""):
            print(QMessageBox.warning(self, "警告", "请插入图片", QMessageBox.Yes, QMessageBox.Yes))
            return
        now = int(time.time())
        timeStruct = time.localtime(now)
        self.strTime = time.strftime("%Y/%m/%d %H:%M", timeStruct)
        self.carid = 'c' + str(time.strftime("%g%m%d")) + str(random.randint(0, 9999)).zfill(4)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myOCR.db')
        db.open()
        query = QSqlQuery()
        sql = "select * from records where RecordId = '%s'"%(self.carid)
        query.exec_(sql)
   
        self.text = "车牌号码：" + 号牌号码 + "\n车辆类型：" + 车辆类型 +"\n所有人：" + 所有人 +"\n使用性质：" + 使用性质 +"\n品牌型号："+品牌型号+"\n车辆识别代号：" + 车辆识别代号 +"\n发动机号："+ 发动机号码 + "\n注册日期："+注册日期 +"\n发证日期："+ 发证日期
        sql = "insert into records values('%s','%s','%s','行驶证识别','%s','')"%(
            self.carid,self.filePath,self.strTime,self.text)
        query.exec_(sql)
        db.commit()
        db.close()
        print(QMessageBox.information(self, "提醒", "已成功识别行驶证!信息可能有误，请仔细核对信息！！！", QMessageBox.Yes, QMessageBox.Yes))
        self.tedit.setPlainText(self.text)

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    carrecognizeWindow = CarCardRecognize()
    carrecognizeWindow.show()
    sys.exit(app.exec_())