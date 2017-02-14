# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
  
            index = inorder.index(postorder.pop(-1))
            root = TreeNode(inorder[index])
            root.right = self.buildTree( inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[0:index], postorder)
            return root