class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        value = []
        for i in range(m):
            for j in range(n):
                if i == 0:
                    value.append(1)
                else:
                    value.append(0)
            dp.append(value)
            dp[i][0] = 1
            value = []
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[m-1][n-1]