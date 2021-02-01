x=-123
z=str(x)
if x>=0:
    x=int(z[::-1])
else:
    x=-int(z[:0:-1])
if -2**31<x<2**31-1:
    print(x)
else:
    print(0)
