# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to anchor the head of the list
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Step 2: Find the k-th node from groupPrev
            kth = self.getKth(groupPrev, k)
            
            # Base Case: If there aren't k nodes left, keep as-is and stop
            if not kth:
                break
                
            groupNext = kth.next

            # Step 3: Local reversal loop (reversing the k-group)
            # Starting prev = groupNext automatically connects the tail 
            # of this reversed group to the start of the next group!
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Step 4: Stitch groupPrev to the new head and advance groupPrev
            tmp = groupPrev.next  # Save reference to the old head (now the tail)
            groupPrev.next = kth  # Connect previous group to the new head (kth)
            groupPrev = tmp       # Move groupPrev to the end of this group for next round

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> ListNode:
        """Helper to advance k steps from curr. Returns None if < k nodes exist."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr