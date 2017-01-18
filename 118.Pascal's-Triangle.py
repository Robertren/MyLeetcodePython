class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        counter = 3
        if numRows == 1:
            result.append([1])
        if numRows == 2:
            result.append([1])
            result.append([1,1])
        if numRows >= 3:
            value = []
            result.append([1])
            result.append([1,1])
            counter = 3
            while counter <= numRows:
                temp = result[-1]
                for i in range(len(temp)-1):
                    value += [temp[i] + temp[i+1]]
                value = [1] + value + [1]
                result.append(value)
                value = []
                counter += 1
                    
        return result
        