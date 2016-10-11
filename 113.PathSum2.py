# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        self.recordPath(root,sum,[])
        return Solution.res
    
    
    def recordPath(self, root, sum, value_list):
        if root == None:
            value_list = []
            return 
        if root.left == None and root.right == None:
            if root.val == sum:
                Solution.res.append(value_list+[root.val])
            return
        self.recordPath(root.left, sum - root.val, value_list+[root.val])
        self.recordPath(root.right, sum - root.val, value_list+[root.val])

        
        
