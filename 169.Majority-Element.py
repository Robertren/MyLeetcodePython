class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = {}
        for i in nums:
            if i in list1:
                list1[i] += 1
            else:
                list1[i] = 1
        
        list1 = sorted(list1.items(), key = lambda x:x[1], reverse =True)
        return list1[0][0]
        