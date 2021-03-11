def isValid(s):
    d={')':'(',']':'[','}':'{'}
    stack=[]
    for i in s:
        if i not in d:
            stack.append(i)
        else:
            if stack.pop()!=d[i]:
                return False
    return not stack

s="{[]}"
print(isValid(s))
