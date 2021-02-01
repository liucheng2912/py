def order(l1):
    if len(l1)<2:
        return l1
    left=[]
    right=[]
    mid = l1[len(l1)//2]
    l1.remove(mid)
    for i in l1:
        if i<mid:
            left.append(i)
        else:
            right.append(i)
    return order(left)+[mid]+order(right)

print(order([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]))