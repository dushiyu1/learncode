
# encoding:utf-8

import requests
import base64
import json
#头文件配置信息
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Gz8YooMGDOGdBCgz9GEmQN3Z&client_secret=XHD7noXfQdmeyxYsWUPQbnvVBFOVCLTo'

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

    print("号牌号码："+号牌号码)
    print("车辆类型："+车辆类型)
    print("所有人："+所有人)
    print("使用性质："+使用性质)
    print("品牌型号："+ 品牌型号)
    print("车辆识别代号："+车辆识别代号)
    print("发动机号码："+发动机号码)
    print("注册日期："+注册日期)
    print("发证日期："+发证日期)