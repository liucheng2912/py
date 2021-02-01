nums=[5,7,7,8,8,10]

def get1(n,target):
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    if target in dict:
            return dict[target]
    else:
        return 0

print(get1(nums,8))

