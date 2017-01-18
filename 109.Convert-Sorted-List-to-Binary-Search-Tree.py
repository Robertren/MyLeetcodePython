# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next

        result = None
        result = self.findnode(list1, result)
        
        return result
        
        
    def findnode(self, list1, root):
        if len(list1) == 0: return 
        if len(list1) == 1:
            pos = 0
        if len(list1) % 2 == 1:
            pos = len(list1) / 2
        else:
            pos = len(list1) / 2 - 1
        root = TreeNode(list1[pos])
        root.left = self.findnode(list1[0: pos], root.left)
        root.right = self.findnode(list1[pos+1:], root.right)
        
        return root