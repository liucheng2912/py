"""
os模块  对文件 目录的操作
os.mkdir() 创建目录
os.removedirs() 删除文件
os.getcwd()  获取当前目录
os.path.exists(dir or file) 判断文件或目录是否存在
"""
import os

# os.mkdir("testdir")
# print(os.listdir("./"))
#
# os.removedirs("testdir")
# print(os.getcwd())

print(os.path.exists("os/b"))
# 判断有没有这个路径或者文件
if not os.path.exists("os/b"):
    os.mkdir("os/b")
if not os.path.exists("os/b/1.txt"):
    with open("os/b/1.txt", "w") as f:
        f.write("hello")