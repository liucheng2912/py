'''
思路：
    将数组进行相加，然后判断是否在querytime中
'''
def f(starttime,endtime,querytime):
    temp=0
    for i in range(len(starttime)):
        if querytime>=starttime[i] and querytime<=endtime[i]:
            temp+=1
    return temp

startTime = [4]
endTime = [4]
queryTime = 5
print(f(startTime, endTime, queryTime))
