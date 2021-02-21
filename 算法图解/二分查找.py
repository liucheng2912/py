'''
基线条件 假如相等，则找到
递归条件 假如大于中值，则在中值和右边进行查找，假如小于中值，则在中值和左边进行查找，
'''
def div_search(l,item):
    mid=l[len(l)//2]
    if mid>item:
        return div_search(l[:mid-1],item)
    elif mid<item:
        return div_search(l[mid+1:],item)
    elif mid==item:
        return True
    return None
