class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        minimum = left

        if (minimum > 0) and nums[0] <= target <= nums[minimum-1]:
            left = 0
            right = minimum - 1
        else:
            left = minimum
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1
