class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1 

        for i in nums:
            if count[i] > 1:
                return True
        
        return False