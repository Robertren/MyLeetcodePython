class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        list1 = set(nums1)
        list2 = set(nums2)
        dict1 = {}
        for i in list1:
            dict1[i] = i
        for i in list2:
            if i in dict1:
                result.append(i)
        
        return result