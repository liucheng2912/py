"""
猴子吃桃问题：
猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
思路：
1 m
2 m/2-1
3（m/2-1）/2-1
反推
10 1  m
9 n/2-1=1  z=2*(m+1)
8 n/2-1=z  n=2*(z+1)
第一天 m
"""
m=1
for i in range(9,0,-1):
    m=2*(m+1)
print(m)
