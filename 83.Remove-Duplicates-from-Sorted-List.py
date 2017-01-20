class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        dummy = ListNode(0)
        dummy.next = temp
        if head == None:
            return head
        if temp.next == None:
            return head
        latter = temp.next
        val_list = []
        val_list.append(temp.val)
        while latter.next != None:
            if latter.val in val_list:
                temp.next = latter.next
                latter = temp.next
            else:
                val_list.append(latter.val)
                latter = latter.next
                temp = temp.next
        if latter.val in val_list:
            temp.next = None
        return dummy.next
        