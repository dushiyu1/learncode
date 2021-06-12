import requests
import json
# 智能回复 Python示例代码


if __name__ == '__main__':
    url = 'https://jisuapiareacode.api.bdymkt.com/iqa/query'
    a = input("你想问啥子呦？？？")
    params = {}
    params['question'] = a
    
    
    headers = {
        
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/63a3e60e767d4761b2a525730d461fc6'
    }
    r = requests.request("POST", url, params=params, headers=headers)
 
    print(r.json()["result"]["content"])