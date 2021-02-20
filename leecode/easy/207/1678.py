'''
思路：
使用字符串的replace进行替换
'''
def f(command):
    command=command.replace('()','o')
    command=command.replace('(al)','al')
    return command

command = "G()()()()(al)"
print(f(command))