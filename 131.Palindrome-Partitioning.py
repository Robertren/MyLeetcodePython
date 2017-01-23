class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.judge(s, [])
        return Solution.res
        
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
            
    def judge(self, s, value_list):
        if len(s) == 0: return Solution.res.append(value_list)
        for i in xrange(1,len(s) + 1):
            if self.isPalindrome(s[0: i]):
                self.judge(s[i:], value_list + [s[:i]])
            