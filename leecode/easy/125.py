'''
先将字符串去除掉空格
然后左右指针比较，判断是否相等
'''
def f(s):
    s1=[]
    for i in s:
        if i.isdigit()==True or i.isalpha()==True:
            s1+=i
    s=''.join(s1).lower()
    if len(s)<2:return True
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s="A man, a plan, a canal: Panama"
print(f(s))