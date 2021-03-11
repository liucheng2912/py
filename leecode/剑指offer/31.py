def validateStackSequences(pushed, popped):
    A = []
    i=0
    for num in pushed:
        A.append(num)
        while A and A[-1]==popped[i]:
            A.pop()
            i+=1
    return not A


pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))