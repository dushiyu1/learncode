import requests
import json
#url = "https://restapi.amap.com/v3/direction/walking?key=cf4185670fcb00ee377f3d5ae9db018b&origin=116.481028,39.989643&destination=116.434446,39.90816&output=JSON"
key = "cf4185670fcb00ee377f3d5ae9db018b"
qidianjing = str(116.481028)
qidianwei = str(39.989643)
zhongdianjing = str(116.434446)
zhongdianwei = str(39.90816)

url = "https://restapi.amap.com/v3/direction/walking?key="+key+"&origin="+qidianjing+","+qidianwei+"&destination="+zhongdianjing+","+zhongdianwei+"&output=JSON"
#print(url)

a = requests.get(url)

if a:
    print(a.json())



