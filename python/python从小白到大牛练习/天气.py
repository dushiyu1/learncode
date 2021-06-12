import requests
import json
# 天气预报查询POST Python示例代码
if __name__ == '__main__':
    url = 'http://gwgp-n6uzuwmjrou.n.bdcloudapi.com/weather/query'
    params = {}
    params['city'] = '台州'
    params['cityid'] = ''
    params['citycode'] = ''
    params['location'] = ''
    params['ip'] = ''
    
    
    headers = {
        
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/63a3e60e767d4761b2a525730d461fc6'
    }
    r = requests.request("POST", url, params=params, headers=headers)
    print(r.json())

