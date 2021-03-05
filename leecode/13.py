'''
思路：
    遍历字符
    当字符为IXC的时候，判断后一位是否是可以拼接的，然后将值加起来
'''
def romanToInt(s):
    res = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(s) == 0: return 0
    for i in range(len(s) - 1):
        if d[s[i]] < d[s[i + 1]]:
            res -= d[s[i]]
        else:
            res += d[s[i]]
    return res + d[s[-1]]

s="LVIII"
print(romanToInt(s))