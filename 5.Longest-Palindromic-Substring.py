class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        # time limit exceed
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s
        start = 0
        end = len(s) - 1
        relength = 0
        result = s[0]
        for i in xrange(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    pass
                else:
                    tmp = s[i:j+1]
                    length = len(tmp)
                    for k in xrange(length):
                        if tmp[k] != tmp[length-1-k]:
                            break
                    if k == length - 1 and length > relength:
                        result = tmp
                        relength = length
                        
        return result
        
class Solution:
    # @return a string
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i)
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome
        