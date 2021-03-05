student={'小萌':'1001','小智':'1002','小强':'1003','info':['A','B','C']}
st = student.copy()
print(st)
st['小萌']='1004'
print(st)
print(student)

st['info'].remove('A')
print(st)
print(student)