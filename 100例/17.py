"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
思路：
1、输入
input
2、分析
英文字母
空格
数字
其他字符
遍历字符的内容
缺点：
如何判断
引入string模块
isalpha()
isdigit()
isspace()
"""
import string
n=input()
x,y,z,w=0,0,0,0
for i in n:
    if i.isalpha():
        x+=1
    elif i.isdigit():
        y+=1
    elif i.isspace():
        z+=1
    else:
        w+=1
print(x,y,z,w)

