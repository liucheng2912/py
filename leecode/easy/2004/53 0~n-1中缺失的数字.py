num=[0,1,2,3,4,5,6,7,9]
def get1(num):
    i, j = 0, len(num) - 1
    while i<=j:
        mid=(i+j)//2
        if num[mid]==mid:
            i=mid+1
        else:
            j=mid-1
    return i

print(get1(num))
