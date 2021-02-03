"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
思路：
1、首先存放英文类型
2、输入一个字母
3、判断这个字母和首字母的关系

"""

a=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

s=input()
for i in a:
    m=s[0]
    n=i[0]


    if m==n:
        if m == 'T' or m == 'S':
            m = s[1]
            n = i[1]
            if m==n:
                print(a.index(i) + 1)
        else:
            print(a.index(i)+1)



