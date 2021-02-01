def qs(arr1):
    if len(arr1)<2:
        return arr1
    mid=arr1[len(arr1)//2]
    left=[]
    right=[]
    arr1.remove(mid)
    for i in arr1:
        if i <mid:
            left.append(i)
        else:
            right.append(i)
    return qs(left)+[mid]+qs(right)

print(qs([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]))