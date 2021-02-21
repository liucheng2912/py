'''
题意：
    用输入的数字进行计算
    输入N 选择一个x，使得N%x==0
    然后N=N-1
    直到无法拿到x
    确认爱丽丝是否成功
    只要计算是否进行了奇数次的运算即可
'''
def divisorGame(N):
    return N%2==0

N=2
print(divisorGame(N))