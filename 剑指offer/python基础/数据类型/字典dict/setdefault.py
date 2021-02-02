dict1={'小萌':1001,'小智':1002,'小强':1003}
dict1.setdefault('小萌')
print(dict1['小萌'])

dict1.setdefault('小军')
print(dict1['小军'])

dict1.setdefault('小红','1004')
print(dict1['小红'])