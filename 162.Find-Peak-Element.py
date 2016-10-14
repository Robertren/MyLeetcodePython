 class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        temp = 0
        list1 = {}
        while i < len(nums):
            if nums[i]>temp or i == 0:
                temp = nums[i]
                list1["max"] = i
            i += 1
        return list1["max"]
            