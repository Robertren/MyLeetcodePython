class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        list1 = s.split(" ")
        list1 = [x for x in list1 if x != ""]
        if list1 != None:
            result_list = list1[::-1]
            return " ".join(result_list)
        else: 
            return ""
        
        