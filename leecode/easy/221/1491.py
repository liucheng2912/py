'''
思路：
    对工资表进行排序，然后去掉收尾两个元素，再计算平均值
    特殊情况 工资表长度小于等于2
'''
from functools import reduce

def avergae(salary):
    if len(salary)<=2:return 0
    else:
        salary = sort1(salary)
        n = len(salary)-1
        result = sum(salary[1:n])/(n-1)
        return '{:.5f}'.format(result)



def sort1(salary):
    if len(salary)<=1:return salary
    else:
        l1=[]
        l2=[]
        pivot = salary[0]
        for i in salary[1:]:
            if i<pivot:
                l1.append(i)
            else:
                l2.append(i)
        return sort1(l1)+[pivot]+sort1(l2)

salary = [4000,3000,1000,2000]
print(avergae(salary))