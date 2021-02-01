def getLeastNumbers(arr,k):
    def kssort(arr):
        l1=[]
        l2=[]
        if len(arr)<2:return arr
        mid=arr[len(arr)//2]
        arr.remove(mid)
        for i in arr:
            if i>mid:
                l2.append(i)
            else:
                l1.append(i)
        return kssort(l1)+[mid]+kssort(l2)
    l1=kssort(arr)
    print(l1)
    return l1[:k]

arr=[0,0,1,2,4,2,2,3,1,4]
k=8
print(getLeastNumbers(arr,k))