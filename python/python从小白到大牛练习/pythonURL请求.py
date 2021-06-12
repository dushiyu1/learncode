from http.client import responses
import urllib.request
import ssl
import json
context = ssl._create_unverified_context()
with urllib.request.urlopen("https://dushiyu1.github.io/post/blog4/",context=context)as response:

    data = response.read()
    html = data.decode("utf-8")
    print(html)

