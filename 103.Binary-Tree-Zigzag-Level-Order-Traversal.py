# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([(root,1)])
        dic = {}
        dic[1] =[root.val]
        result = []
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
                if level + 1 not in dic:
                    dic[level+1] = [node.left.val]
                else:
                    dic[level+1] += [node.left.val]
            if node.right:
                queue.append((node.right, level+1))
                if level + 1 not in dic:
                    dic[level+1] = [node.right.val]
                else:
                    dic[level+1] += [node.right.val]
        for i in dic:
            if i % 2 == 1:
                result.append(dic[i])
            else:
                result.append(dic[i][::-1])
        return result