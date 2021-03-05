'''
思路：
    首先搜索一级关系，假如一级关系的节点不符合要求，将一级关系的一级关系加入到队列中进行查找
    假如搜索到或者是队列长度为0，退出程序
    需要加一个标志位用于判断是否已经搜索过了，以免出现死循环效果
'''
from collections import deque
graph={}
graph['you']=['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['thom','jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]

def person_is_seller(person):
    return person[-1]=='m'

def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return True
            else:
                search_queue+=graph['person']
                searched.append(person)
    return False


