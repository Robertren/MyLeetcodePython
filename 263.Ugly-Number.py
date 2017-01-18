class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        result = self.judge(num)
        return result

        
    def judge(self, num):
        if num in [2, 3, 5]: return True
        if num % 2 == 0:
            return self.judge(num / 2)
        elif num % 5 == 0:
            return self.judge(num / 5)
        elif num % 3 == 0:
            return self.judge(num / 3)
        else: return False