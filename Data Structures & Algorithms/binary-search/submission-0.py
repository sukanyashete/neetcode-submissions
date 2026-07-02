class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        if target == nums[low]:
            return low
        elif target == nums[high]:
            return high

        while (low <= high):
            mid = int(low + ((high-low)/2))
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid

        return -1
        