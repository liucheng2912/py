"""
题目：练习函数调用。
程序分析：使用函数，输出三次 RUNOOB 字符串。
思路：
函数定义
函数调用 循环调用三次
缺点：
if __name__=='__main__'的用法
"""
def f():
    print('RUNOOB')
def f1():
    for i in range(3):
        f()
if __name__=='__main__':
    f1()