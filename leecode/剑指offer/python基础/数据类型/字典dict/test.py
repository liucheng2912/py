#字典使用
#key 为唯一的，不可变的类型
dict1={'小萌':1001,'小智':1002,'小强':1003}
dict2={'abc':456}
dict3={'abc':123,98.65:37}

#student=[('name':'小萌'),('number':'1001')]
#使用dict函数声明字典
details = dict(name='小萌',number=10001)
print(details)
print(details['name'])

#修改字典
student={'小萌':'1001','小智':'1002','小强':'1003'}
student['小强']='1004'
print('小强的学号是%(小强)s'%student)

student['小张']='1005'
print('小张的学号是%(小张)s'%student)
print(len(student))
#删除字典
del student['小张']
print(len(student))
print(type(student))
print(student)

#删除整个字典
#del student
print(student)
