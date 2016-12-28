# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        result = []
        stack  = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                result.append(level + 1)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return max(result)

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
            