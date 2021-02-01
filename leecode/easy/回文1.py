#反转判断是否相等
x = 0
x1 = str(x)
if x>=0:
    y = int(x1[::-1])
    if x==y:
        print("True")
else:
    print("False")