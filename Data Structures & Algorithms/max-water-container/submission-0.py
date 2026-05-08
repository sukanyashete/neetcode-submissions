class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        volume = -float('inf')
        while left < right:
            vol = (right-left)*min(heights[left], heights[right])
            volume = max(volume, vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return volume

        