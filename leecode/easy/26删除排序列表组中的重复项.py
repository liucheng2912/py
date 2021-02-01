class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=len(nums)-1
        if i==-1:return 0
        if i==0:return nums
        while i>0:
            if nums[i-1]==nums[i]:
                del nums[i]
            i=i-1

        return nums

if __name__ =='__main__':
    a = Solution()
    print(a.removeDuplicates([1]))