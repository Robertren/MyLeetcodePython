class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list1 = str.split()
        temp = []
        if len(list1) != len(pattern):
            return False
        lookup = {}
        for i in range(len(list1)):
            if pattern[i] in lookup:
                if lookup[pattern[i]] != list1[i]:
                    return False
            elif list1[i] in temp:
                return False
            else:
                lookup[pattern[i]] = list1[i]
                temp.append(list1[i])

        
        return True