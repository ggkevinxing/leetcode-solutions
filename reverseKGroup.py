# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head
        nextHead = head
        for _ in range(k - 1):
            nextHead = nextHead.next
            if nextHead is None:
                return head
        
        prev = None
        curr = head
        for i in range(k):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        head.next = self.reverseKGroup(curr, k)
        
        return nextHead