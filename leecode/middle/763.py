'''
思路：
    需要满足每个片段的字符不在另外的片段中，且最小
    left指向0
    right指向0
    找到第一个元素最后出现的位置
    然后left+1 查找第二个元素出现的最后位置，right扩张

'''
def f(S):
    d={s:index for index,s in enumerate(S)}
    nums=0
    left=0
    # 更新right为第一个字符最后的index
    right=d[S[left]]
    res=[]
    while left<len(S):
        nums += 1
        #left右移
        #假如第二个字符的最后index大于right，更新
        if right<d[S[left]]:
            right=d[S[left]]
        #假如left和right相等了
        if left==right:
            res.append(nums)
            nums=0
        left+=1
    return res

S = "ababcbacadefegdehijhklij"
print(f(S))
