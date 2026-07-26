class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Keep merging pairs until only 1 list remains
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # If i + 1 is out of bounds, l2 is None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                mergedLists.append(self.mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]

    # Standard helper: Merge 2 Sorted Lists
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next