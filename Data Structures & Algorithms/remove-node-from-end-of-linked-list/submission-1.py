# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0

        while curr != None:
            curr = curr.next
            cnt += 1

        pos = cnt - n
        curr = head

        if pos == 0:
            return head.next

        while pos > 0:
            prev = curr
            curr = curr.next
            pos -= 1
        
        #if curr:
        prev.next = curr.next
        #else:
        #    prev.next = None

        return head
