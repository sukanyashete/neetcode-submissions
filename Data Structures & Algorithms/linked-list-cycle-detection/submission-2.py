# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Logic explanation:
# 1 - If the list is empty (head is None): fast is None. 
# The while loop condition immediately evaluates to false, skips the loop entirely and returns False.
# 2 - If the list has no cycle: fast (or fast.next) will eventually hit None, the loop will safely terminate, and return False.
# 3 - If there is a cycle: fast will never hit None, the loop will run continuously until fast laps slow, 
# matching if slow == fast: condition and returning True
