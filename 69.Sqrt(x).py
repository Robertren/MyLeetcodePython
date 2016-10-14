class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        first = 0
        second = x
        mid = (first + second)/2
        if x == 1:
            return 1
        while first <= second:
            if  mid ** 2 < x:
                first = mid
            elif mid ** 2 > x:
                second = mid
            else:
                return mid
            mid = (first + second)/2
            if second - first == 1:
                break
            
        return mid