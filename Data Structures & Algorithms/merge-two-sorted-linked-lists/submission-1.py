# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if not curr1:
            return curr2
        if not curr2:
            return curr1

        if curr1.val <= curr2.val:
            ret = curr1
            curr1 = curr1.next
        else:
            ret = curr2
            curr2 = curr2.next
        
        curr = ret

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next

            else:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next

        if not curr1:
            #ptr = curr2
            curr.next = curr2
        else:
            #ptr = curr1
            curr.next = curr1

        #while curr!= None:
        #    curr.next = ptr
        #    ptr = ptr.next

        return ret
