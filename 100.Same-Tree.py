# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        plist = [(p.val, 0)] 
        pstack = [(p,0)]
        while pstack:
            node, level = pstack.pop()
            if not node:
                plist.append(("null",level+1))
            if node.left:
                pstack.append((node.left, level+1))
                plist.append((node.left.val, str(level+1)+"left"))
            if node.right:
                pstack.append((node.right, level+1))
                plist.append((node.right.val,  str(level+1)+"right"))
        qlist = [(q.val,0)]
        qstack = [(q, 0)]
        while qstack:
            node,level = qstack.pop()
            if not node:
                qlist.append(("null",level+1))
            if node.left:
                qstack.append((node.left, level+1))
                qlist.append((node.left.val,  str(level+1)+"left"))
            if node.right:
                qstack.append((node.right, level+1))
                qlist.append((node.right.val,  str(level+1)+"right"))
        if qlist == plist:
            return True
        else:
            return False
        # recursion
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p == q