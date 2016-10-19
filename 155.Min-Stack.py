class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        MinStack.solution = []
        MinStack.get_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (len(MinStack.get_min) == 0 or MinStack.get_min[-1] >= x):
            MinStack.get_min.append(x) 
        MinStack.solution.append(x)
            
    def pop(self):
        """
        :rtype: void
        """
        if len(MinStack.solution) == 0:
            return False
        else:
            if  MinStack.solution[-1] == MinStack.get_min[-1]:
                MinStack.get_min.pop()
            MinStack.solution.pop()
    def top(self):
        """
        :rtype: int
        """
        if len(MinStack.solution) == 0:
            return None
        else:
            return MinStack.solution[-1]

    def getMin(self):
        """
        :rtype: int
        """
        result = MinStack.get_min[-1]
        return result
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()