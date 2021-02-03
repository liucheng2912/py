"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
思路：
输入n和a n代表几个数相加 a代表值
遍历n
1 a
2 a*10+a
3 a*100+a*10+a+a*10+a+a
x max=a*10^(x-1)+a*10^(x-2)+...a*10^0
  max-1=a*10^(x-2)+...a
优化：
可以使用functools的reduce模块 
"""
n=int(input())
a=int(input())

sum=0
if n<0:
    print('error')
if n==0:
    print(0)
for n in range(n,0,-1):
    num = 0
    while n>0:
        num+=a*10**(n-1)
        n-=1
    print(num)
    sum+=num
print(sum)
