l1=[2,3,5,4,9,6]

def order(l1):
    if len(l1)<2:
        return l1
    left=[]
    right=[]
    mid = l1[len(l1)//2]
    l1.remove(mid)
    for i in l1:
        if i <mid:
            left.append(i)
        else:
            right.append(i)
    return order(left)+[mid]+order(right)

print(order(l1))