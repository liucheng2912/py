nums=[1,2,3,1]
k=3
dict={}

for i in range(len(nums)):
    #dict={1:0,2:1,3:2}
    if nums[i] in dict.keys():
        #nums[3]=1 in dict
        #3-dict[1]=3-0<=k
        if i - dict[nums[i]]<=k:
            print(True)
        else:
            dict[nums[i]]=i
    else:
        dict[nums[i]]=i

print(dict)