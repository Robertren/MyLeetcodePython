class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums2:
            if i in nums1:
                result.append(i)
                nums1[nums1.index(i)] = 'a'
        return result