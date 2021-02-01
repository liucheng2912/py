import requests

r=requests.get("http://www.baidu.com")

print(r.status_code)
print(r.encoding)
r.encoding="utf-8"
print(r.encoding)

r1=requests.post("http://httpbin.org/post",data={'key':'value'})
print(r1.text)