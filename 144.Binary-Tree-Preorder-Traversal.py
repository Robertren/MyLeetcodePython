class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        top = root
        result = []
        stack = []
        while top or stack:
            if top == None:
                top = stack.pop()
            result.append(top.val)
            if top.right:
                stack.append(top.right)
            top = top.left
        return result