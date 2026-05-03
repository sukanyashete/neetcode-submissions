class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        #index = 0
        for index, num in enumerate(nums):
            if (target - num) in idx:
                return [idx[target-num], index]
            else:
                idx[num] = index
                #index += 1

