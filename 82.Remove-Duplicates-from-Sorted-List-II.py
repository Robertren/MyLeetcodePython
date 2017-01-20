class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp =  ListNode(0)
        dummy.next = temp
        dup_list = []
        result_list = []
        if head == None:
            return None
        while head.next != None:
            if head.val in dup_list:
                pass
            elif head.val in result_list :
                result_list.remove(head.val)
                dup_list.append(head.val)
            else:
                result_list.append(head.val)
            head = head.next
        if head.val not in result_list and head.val not in dup_list:
            result_list.append(head.val)
        elif head.val in result_list :
            result_list.remove(head.val)
        for i in result_list:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next.next