def f(l:list,item):
    mid=len(l)//2
    guess=l[mid]
    if guess==item:
        return mid
    elif guess>item:
        return f(l[:mid-1],item)
    elif guess<item:
        return f(l[mid+1:],item)
    else:
        return None
