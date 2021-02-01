s1="i have a student"
s2="aeiou"

l=list(s1)
for i in l:
    if i in s2:
        l.remove(i)
print(l)
l=''.join(l)
print(l)