'''
思路：
    遍历worker，difficulty中第一个小于worker的值
    left指向difficulty，找到第一个大于worker的值
    用字典存放
    然后worker指针向右，比较left指向的值，假如小于
    则假如
    大于，则向右
'''
def f(difficulty,profit,worker):
    list1=sorted(map(tuple,zip(difficulty,profit)))
    worker.sort()
    re1,right,res=0,0,0
    for i in worker:
        while right<len(list1) and list1[right][0]<=i:
            re1 = max(re1,list1[right][1])
            right+=1
        res+=re1
    return res
difficulty = [85,47,57]
profit =[24,66,99]
worker =[40,25,25]



print(f(difficulty, profit, worker))
