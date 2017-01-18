
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if not root:
            return 0
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                result.append(depth + 1)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return min(result)