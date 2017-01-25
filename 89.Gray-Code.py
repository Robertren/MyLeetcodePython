class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        value = ""
        Solution.res = []
        result = []
        self.findcode(n, "")
        for i in Solution.res:
            result.append(int(i, 2))
        return result
        
        
    
    
    def findcode(self, n, value):
        if n == 0: return Solution.res.append(value)
        count = 0
        for i in value:
            if i == "1":
                count += 1
        if value == "":
            self.findcode(n - 1, value + "0")
            self.findcode(n - 1, value + "1")
        elif count % 2 == 0:
            self.findcode(n - 1, value + "0")
            self.findcode(n - 1, value + "1")
        elif count % 2 == 1:
            self.findcode(n - 1, value + "1")
            self.findcode(n - 1, value + "0")
            
        