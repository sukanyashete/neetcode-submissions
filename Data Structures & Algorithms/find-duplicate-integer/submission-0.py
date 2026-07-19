class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        for i in range(len(nums)):
            fast, slow1 = 0, 0
            slow2 = 0

            while True:
                slow1 = nums[slow1]
                fast = nums[nums[fast]]
                if fast == slow1:
                    break

            while True:
                slow2 = nums[slow2]
                slow1 = nums[slow1]
                if slow1 == slow2:
                    return slow1 # can return any because both are pointing to the same.
