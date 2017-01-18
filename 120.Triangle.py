# Recusion pass 42/ 43 test case
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        Solution.res = []
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        for i in xrange(len(triangle[-1])):
            self.sum(0, [i, i-1], triangle)
        return min(Solution.res)
    def sum(self, sum1, pos, list1):
        #print pos
    
        if len(list1) == 1: 
            return Solution.res.append(sum1 + list1[0][0])
            # if list1[0][pos] >= list1[0][pos + 1]:
            #     return Solution.res.append(sum1 + list1[0][pos + 1])
            # else:
            #     return Solution.res.append(sum1 + list1[0][pos])
        for i in xrange(len(list1[-1])):
            if i in pos:
                self.sum(sum1 + list1[-1][i], [i,i-1], list1[0:-1])

         