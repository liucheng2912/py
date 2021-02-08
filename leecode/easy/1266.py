'''
思路：

'''
def f(points):
    x0, x1 = points[0]
    ans=0
    for i in range(1,len(points)):
        y0,y1=points[i]
        ans+=max(abs(x0-y0),abs(x1-y1))
        x0,x1=points[i]
    return ans


points = [[1,1],[3,4],[-1,0]]
print(f(points))