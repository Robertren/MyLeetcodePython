# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        final_list = {}
        from collections import deque
        queue = deque([(root,0)])
        final_list[0] = [root.val]
        result = []
        while queue:
            node,level = queue.popleft()
            if node.left:
                if level + 1 not in final_list:
                    final_list[level + 1] = [node.left.val]
                else:
                    final_list[level + 1] += [node.left.val]
                queue.append((node.left, level + 1))
            if node.right:
                 if level + 1 not in final_list:
                    final_list[level + 1] = [node.right.val]
                 else:
                    final_list[level + 1] += [node.right.val]
                 queue.append((node.right, level + 1))
        for i in final_list.keys():
            result.append(final_list[i])
        return result