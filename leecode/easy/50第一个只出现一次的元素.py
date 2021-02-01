s = "leetcode"
def get1(s):
    dict = {}
    if len(s) == 1: return s[0]
    if len(s) == 0: return " "
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        if dict[i] == 1:
            return i
    return " "
print(get1(s))


