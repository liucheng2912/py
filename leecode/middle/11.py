'''
思路：
    双指针
    假如左边小于右边，则左边向内移动，否则右边向内移动
'''
def f(height):
    left,right,res=0,len(height)-1,0
    while left<right:
        if height[left]<height[right]:
            res=max(res,height[left]*(right-left))
            left+=1
        else:
            res=max(res,height[right]*(right-left))
            right-=1
    return res

h=[1,1]
print(f(h))