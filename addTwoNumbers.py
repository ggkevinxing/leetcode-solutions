# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryOver = 0
        lenL1 = 0
        lenL2 = 0

        # find which node is greater length
        l1Temp = l1
        l2Temp = l2
        while l1Temp != None:
            lenL1 += 1
            l1Temp = l1Temp.next
        while l2Temp != None:
            lenL2 += 1
            l2Temp = l2Temp.next

        if lenL2 > lenL1:
            first = l2
            second = l1
        else:
            first = l1
            second = l2

        # surely there is a more elegant solution than this
        l1Temp = first
        l2Temp = second
        temp = ListNode(0)
        head = temp
        while temp != None:
            if l1Temp and l2Temp:
                temp.val = l1Temp.val + l2Temp.val + carryOver
            elif l1Temp:
                temp.val = l1Temp.val + carryOver
            elif l2Temp:
                temp.val = l2Temp.val + carryOver
            else:
                temp.val = carryOver
            carryOver = 0
            if temp.val >= 10:
                carryOver = 1
                temp.val = temp.val % 10
            if l1Temp.next != None:
                tempNext = ListNode(0)
                temp.next = tempNext
                temp = tempNext
            elif carryOver == 0:
                temp.next = None
                temp = None
            else:
                temp.next = ListNode(carryOver)
                temp = None
            l1Temp = l1Temp.next
            if l2Temp != None:
                l2Temp = l2Temp.next
        print(head)
        return head


