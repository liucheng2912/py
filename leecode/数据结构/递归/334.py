def reverse1(s):
    def reve(start,end,s):
        if start>end:return s
        s[start],s[end]=s[end],s[start]
        return reve(start+1,end-1,s)
    return reve(0,len(s)-1,s)

s=['h','e','l','l','o']
print(reverse1(s))