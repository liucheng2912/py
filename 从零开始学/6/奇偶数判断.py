"""
写一个函数判断输入的数字是奇数还是偶数
思路：
1、函数声明
2、输入
3、判断
判断语句
"""
def fun1(n):
    if n%2==0:
        print('%s是偶数'%n)
    else:
        print('%s是奇数'%n)

n=int(input('请输入数字:'))
fun1(n)