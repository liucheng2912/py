'''
思路：
    遍历数组
    选择位置 前后都为0
'''
def canP(flowerbed,n):
    flowerbed=[0]+flowerbed+[0]
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            n-=1
    return n<=0

flowerbed = [1,0,0,0,1]
n = 1
print(canP(flowerbed, n))


