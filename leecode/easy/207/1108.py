'''
思路：
    使用字符串的replace替换
'''
def f(address):
    return address.replace('.','[.]')

address = "255.100.50.0"
print(f(address))