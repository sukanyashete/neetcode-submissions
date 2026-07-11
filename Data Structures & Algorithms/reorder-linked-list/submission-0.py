# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverseList(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle node
        mid = middleList(head)
        
        # Step 2: Reverse the second half of the list starting from mid
        end = reverseList(mid)
        
        # Step 3: Interleave the two lists cleanly
        start = head
        while end.next:
            tempS = start.next
            tempE = end.next
            
            start.next = end
            end.next = tempS
            
            start = tempS
            end = tempE