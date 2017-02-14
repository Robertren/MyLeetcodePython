class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [0 for x in xrange(len(nums))]
        result1 = [0 for x in xrange(len(nums))]
        best = [0 for x in xrange(len(nums))]
        best[0] = nums[0]
        if nums[0] >= 0:
            result[0] = nums[0]
        else:
            result1[0] = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                best[i] = result1[i-1] * nums[i]
                result[i] = result1[i-1] * nums[i]
                result1[i] =  min(result[i - 1] * nums[i], nums[i])
            else:
                best[i] = max(result[i-1] * nums[i], nums[i])
                result[i] = max(result[i-1] * nums[i], nums[i])
                result1[i] = result1[i - 1] * nums[i]
                
        return max(best)
            