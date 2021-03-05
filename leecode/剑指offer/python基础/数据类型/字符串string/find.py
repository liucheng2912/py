#检测字符串中是否包含子字符串str
field='do it now'

print(field.find('do')) #0
print(field.find('it')) #3 找打就返回索引
print(field.find('python')) #-1 找不到就返回-1

#提供起点 'it now'
print(field.find('it', 2)) #3
#提供起点 'now'
print(field.find('it', 5)) #-1
#提供起点和终点 'do '
print(field.find('it', 0, 3))   #-1
#提供起点和终点 'do it'
print(field.find('it', 0, 5)) #3
#提供起点和终点 'now'
print(field.find('it', 5, 10)) #-1
