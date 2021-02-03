"""
按相反的顺序输出列表的值。
思路：list reverse
缺点：
reverse 返回none 直接作用与list本身
切片
"""
list1=[1,2,3,4]
list1.reverse()
print(list1)

list3=[1,2,3,4]
list2=list3[::-1]
print(list2)