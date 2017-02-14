# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        value = 0
        if not root:
            return 0
        stack = [(root, "")]
        while stack:
            node, digit = stack.pop()
            if not node.left and not node.right:
                result.append(digit + str(node.val))
            if node.left:
                stack.append((node.left, digit + str(node.val)))
            if node.right: 
                stack.append((node.right, digit + str(node.val)))
        for i in result:
            value += int(i)
        return value
                