class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = i
            else:
                temp = i - dict1[nums[i]]
                if temp <= k:
                    return True
                else:
                    dict1[nums[i]] = i
        return False