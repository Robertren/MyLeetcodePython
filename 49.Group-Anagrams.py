class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        keylist = {}
        result = []
        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))
            if temp not in keylist:
                keylist[temp] = strs[i]+','
            else:
                keylist[temp] += strs[i]+','
        for i in keylist:
            list1 = keylist[i][0:-1].split(',')
            result.append(list1)
            list1 = []
        return result