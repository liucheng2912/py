'''
思路：
    首先分隔字符串
    再将每个单词进行反转
    反转可以使用reverse 或者切片
'''
def reverseWords(s):
    l=s.split()
    for i in range(len(l)):
        s=l[i]
        l[i]=s[::-1]
    return ' '.join(l)

s="Let's take LeetCode contest"
print(reverseWords(s))