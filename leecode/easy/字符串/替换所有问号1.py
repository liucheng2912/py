def f(s):
    a='abcdefghijklmnopqrstuvwxyz'
    res=list('0'+s+'0')
    i=1
    while i <len(res)-1:
        if res[i]=='?':
            j=0
            while j<len(a):
                if j not in (res[i-1],res[i+1]):
                    res[i]=a[j]
                    break
                j+=1
        i+=1
    return ''.join(res[1:-1])
