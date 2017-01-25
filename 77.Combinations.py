class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k :
            return []
        Solution.res = []
        self.result(n, k, [])
        re_list = []
        for i in Solution.res:
            if i not in re_list:
                re_list.append(i)
        return re_list
        
    def result(self, n, k, value_list):
        if k == 0: return Solution.res.append(value_list)
        for i in xrange(1, n+1):
            
            if n - 1 >= k:
                self.result(n-1, k, value_list)
            self.result(n-1, k-1, value_list + [n])
# TIME LIMITED EXCEED