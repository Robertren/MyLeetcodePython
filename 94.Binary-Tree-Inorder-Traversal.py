class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        value_list = []
        def inTraversal(root,value_list):
            if root == None:
                return
            if root.left == None and root.right == None:
                value_list += [root.val]
                return
            else:
                inTraversal(root.left, value_list)
                value_list += [root.val]
                inTraversal(root.right,value_list)
        inTraversal(root,value_list)
        return value_list