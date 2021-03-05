def f(l:list,item):
    if len(l)<=1:return 0
    low=0
    high=len(l)-1
    while low<=high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess==item:
            return mid
        elif guess>item:
            high=mid-1
        elif guess<item:
            low=mid+1
    return None
