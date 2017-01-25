class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[-1] < target:
                pass
            else:
                start = 0
                end = len(i) - 1
                mid = (start + end) / 2
                while start <= end:
                    mid = (start + end) / 2
                    if i[mid] < target:
                        start = mid + 1
                    elif i[mid] > target:
                        end = mid - 1
                    else:
                        return True
                return False
        return False