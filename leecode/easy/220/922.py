'''
题意：将偶数放到偶数index上，将奇数放到奇数index上
思路：将偶数和奇数分别取出来，然后放到index上
双指针，一个指针指向偶数位，一个指针指向奇数位，当匹配数据不对时，进行数据交换，然后继续遍历，直到遍历完成
'''
def sortArrayByParityII(A):
    l1=0
    l2=1
    while l1<len(A) and l2<len(A):
        while l1<len(A) and A[l1]%2==0:
            l1+=2
        while l2<len(A) and A[l2]%2!=0:
            l2+=2
        if l1<len(A) and l2<len(A):
            A[l1],A[l2]=A[l2],A[l1]
            l1+=2
            l2+=2
    return A

A=[4,2,5,7]
print(sortArrayByParityII(A))