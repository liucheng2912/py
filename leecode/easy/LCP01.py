"""
思路：
比较两个数组相等的元素个数
"""
def game(guess,answer):
    temp=0
    for i in range(len(guess)):
        if guess[i]==answer[i]:
            temp+=1
    return temp

guess = [1,2,3]
answer = [1,2,3]
print(game(guess, answer))