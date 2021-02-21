'''
思路：
    将数组转换成字符串进行连接
    然后比较
'''
def f(word1,word2):
    word1=''.join(word1)
    word2=''.join(word2)
    return word1==word2

word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(f(word1, word2))