class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

    # Using method to check each number
    # def nthUglyNumber(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #     num = 1
    #     while count < n:
    #         if self.judge(num):
    #             count += 1
    #         num += 1

    #     return num - 1

        
    # def judge(self, num):
    #     if num == 1: return True
    #     if num in [2, 3, 5]: return True
    #     if num % 2 == 0:
    #         return self.judge(num / 2)
    #     elif num % 5 == 0:
    #         return self.judge(num / 5)
    #     elif num % 3 == 0:
    #         return self.judge(num / 3)
    #     else: return False