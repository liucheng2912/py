#暴力拆解法
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            list1=i
            for j in list1:
                if target==j:
                    return True
        return False

if __name__=='__main__':
    a=Solution()
    n=[
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
    result=a.findNumberIn2DArray(n,20)
    print(result)