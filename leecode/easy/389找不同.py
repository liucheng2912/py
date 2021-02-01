def get1(s,t):
    dict={}
    dict1={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for j in t:
        if j not in dict1:
            dict1[j]=1
        else:
            dict1[j]+=1
    for j in t:
        if j not in dict or dict[j]!=dict1[j]:
            return j

s="a"
t="aa"
print(get1(s,t))