n = [2,3,1,0,2,5,3]
#从第一个开始遍历，找到相同的就退出查找
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]==n[j]:
            print(n[i])
            break
    break