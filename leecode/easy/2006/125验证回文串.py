s="race a car"
list1=[]
for i in s:
    if i.isdigit():
        list1.append(i)
    if i.isalpha():
        list1.append(i.upper())
list2=list1[::-1]
if list2==list1:
    print("True")
else:
    print("Fsalse")
print(list1)
print(list2)