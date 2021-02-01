#动态规划算法
#O(N)
n = 10
num1={}
num1[0]=0
num1[1]=1
#从底部开始解决
for i in range(2,n+1):
    num1[i]=num1[i-1]+num1[i-2]

print(num1[n])
