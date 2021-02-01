matrix=[[1,2,3],[4,5,6],[7,8,9]]
def get1(matrix):
    #当matrix为空的时候，直接返回空列表[]
    if not matrix:return []
    #矩阵l,r,t,b四个边界 l用于打印结果列表
    l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
    #循环打印 从左到右 从上到下 从右向左 从下到上
    #根据边界打印，将元素按顺序添加至列表尾部
    #边界向内收缩1，代表已被打印
    #判断是否打印完毕，边界是否相遇，若打印完毕则跳出
    while True:
        #从左向右
        #左边界l,右边界r，t+1，判断是否打印完毕 t>b
        for i in range(l,r+1):
            res.append(matrix[t][i])
        t+=1
        if t>b:break
        #从上到下，上边界t，下边界b，右边界r-1,是否打印完毕l>r
        for i in range(t,b+1):
            res.append(matrix[i][r])
        r-=1
        if l>r:break
        #从右向左，右边界r，左边界l，下边界b-1，是否打印完毕 t>b
        for i in range(r,l-1,-1):
            res.append(matrix[b][i])
        b-=1
        if t>b:break
        #从下到上 下边界b 上边界t 左边界l-1 是否打印完毕l>r
        for i in range(b,t-1,-1):
            res.append(matrix[i][l])
        l+=1
        if l>r:break
    return res

a=get1(matrix)
print(a)








