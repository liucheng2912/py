'''
思路：
    y不存在与x中
    将x存放到set中
    遍历y
    判断y是否在set中
'''
def f(paths):
    s=set()
    for i in range(len(paths)):
        s.add(paths[i][0])
    for j in range(len(paths)):
        if paths[j][1] not in s:
            return paths[j][1]

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(f(paths))
paths = [["B","C"],["D","B"],["C","A"]]
print(f(paths))
paths = [["A","Z"]]
print(f(paths))