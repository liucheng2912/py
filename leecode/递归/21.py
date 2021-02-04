"""
合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
思路：
递归实现 定义一个合并函数，
结束条件，两个链表长度都为空
循环条件，长度会减少
主函数
if l1[i]>l2[j]:
    l.append(l2[j])
    j++
elif l1[i]<l2[j]:
    l.append(l1[i])
    i++
"""
def merge(l1,l2):
    l=[]
    while len(l1) and len(l2):
        n1 = len(l1) - 1
        n2 = len(l2) - 1
        if l1[n1] > l2[n2]:
            l.append(l1[n1])
            l1.remove(l1[n1])
        else:
            l.append(l2[n1])
            l2.remove(l2[n1])
    if len(l1)!=0:
        l.extend(l1)
    if len(l2)!=0:
        l.extend(l2)
    l.reverse()
    return l

if __name__=='__main__':
    l1=[]
    l2=[0]
    print(merge(l1, l2))
