# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0

        if (not p1):
            return p2

        elif (not p2):
            return p1

        else:
            while p1 and p2:
                value = p1.val + p2.val + carry
                carry = value // 10
                value = value % 10
                p1.val = value

                prev = p1
                p1 = p1.next
                p2 = p2.next

            if p2:
                prev.next = p2
                p1 = p2

            if p1:
                while p1 != None:
                    value = p1.val + carry
                    carry = value // 10
                    value = value % 10
                    p1.val = value
                    prev = p1
                    p1 = p1.next

            # Only loop through leftovers while there is an active carry
            if p1 and carry > 0:
                while p1 and carry > 0:
                    value = p1.val + carry
                    carry = value // 10
                    value = value % 10
                    p1.val = value
                    prev = p1
                    p1 = p1.next

            if carry > 0:
                prev.next = ListNode(carry)

        return l1
