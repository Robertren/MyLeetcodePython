class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        templist = [1,1]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex >= 2:
            index = 2
            result = []
            while index <= rowIndex:
                for i in range(len(templist)-1):
                    result += [templist[i] + templist[i+1]]
                result = [1] + result + [1]
                templist = result
                result = []
                index += 1
        return templist
