class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set=set()
        for n in nums:
            if n not in my_set:
                my_set.add(n)
        nums=list(my_set)
        return nums


if __name__ =='__main__':
    a = Solution()
    print(a.removeDuplicates([1,1,2]))