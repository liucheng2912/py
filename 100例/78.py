"""
 person = {"li":18,"wang":50,"zhang":20,"sun":22}
 找出年龄最大的人
"""
person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
max = 'li'
for i in person:
    if person[max]<person[i]:
        max=i
print(max)
