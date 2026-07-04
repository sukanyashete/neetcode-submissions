class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            mid = (left + right) //2
            if (nums[mid] > nums[right]):
                # Min must be in the right half, and mid is not it
                left = mid + 1
            else:
                # Min is either at mid or in the left half
                right = mid

        # When left == right, they point to the minimum element
        return nums[left]
        
