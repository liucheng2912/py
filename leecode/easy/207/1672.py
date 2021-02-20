'''
思路：
将每行的数据进行相加的操作，然后取出最大的一个数
方法
引用reduce方法，将每行的内容进行相加 然后存到一个列表里，取出最大值
也可直接利用sum方法和max方法
'''
def max1(account):
    a=[]
    for i in account:
        a.append(sum(i))
    return max(a)



accounts = [[1,5],[7,3],[3,5]]
print(max1(accounts))