
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
#请求返回的状态码
print(response.status)
#请求返回的相应信息
print(response.read())
#请求头信息
print(response.headers)