'''
思路：
    由于只需要返回整数部分，所以可以通过二分查找
    存在一个整数满足i**2<=n<(i+1)**2
'''

def mySqrt(x):
    low=0
    high=x
    while low<=high:
        mid=(low+high)//2
        if mid**2<=x:
            if (mid+1)**2>x:
                return mid
            elif (mid+1)<=x:
                low=mid+1
        elif mid**2>x:
            high=mid-1
    return None

x=8
print(mySqrt(x))