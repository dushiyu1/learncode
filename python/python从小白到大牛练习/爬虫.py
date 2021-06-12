import requests
from bs4 import BeautifulSoup
data = "打开终端"
url = "https://dushiyu1.github.io/post/blog4/"
r = requests.get(url)
r.encoding = "utf-8"
html = r.text
print(html)
soup = BeautifulSoup(html)
formdata = {"type":"text","keywords":data}
r_r = requests.post(url,formdata)
r_r.encoding = "utf-8"
r_html = r_r.text
print(type(r_html))