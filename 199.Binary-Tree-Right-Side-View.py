class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic = {}
        result = []
        from collections import deque
        queue = deque([(root,1)])
        while queue:
            node, level = queue.popleft()
            if node.right:
                queue.append((node.right,level + 1))
            if node.left:
                queue.append((node.left,level + 1))
            if level in dic:
                dic[level] += [node.val]
            else:
                dic[level] = [node.val]
        for i in dic:
            result.append(dic[i][0])
        return result
            
                