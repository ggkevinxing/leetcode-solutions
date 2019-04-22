# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

    def swapPairs_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        second = head.next
        prev = None
        curr = head
        
        while curr and curr.next:
            # swap logic
            nextHead = curr.next
            curr.next = nextHead.next
            nextHead.next = curr
            if prev:
                prev.next = nextHead
            # don't forget to update prev and curr!
            prev = curr
            curr = curr.next
        return second