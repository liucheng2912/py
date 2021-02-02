a = 155
print(type(a))

b = 155/3
print(type(b))
print(b)

#地板除
c = 155//3
print(type(c))
print(c)

#数据类型转换
b = int(b)
c = float(c)
print(b)
print(type(b))
print(type(c))
print(c)

sum=0
for i in range(16):
    sum+=2**i
print(sum)

habit = "Python 是一门很有用的编程语言\n 我想学好它"
print(habit)
print(len(habit))