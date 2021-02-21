l1=[4,1,2,1,2]

def get1(nums):
   temp=0
   #异或  0和任何数异或为任何数 相同数异或为0
   for i in nums:temp^=i
   return temp

print(get1(l1))
