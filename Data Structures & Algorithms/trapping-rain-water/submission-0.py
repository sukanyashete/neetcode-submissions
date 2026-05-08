class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxLeft, maxRight = 0, 0
        water = 0

        # Water at position i = min(max_Left, max_Right) - height[i]
        while left < right:
            
            if height[left] < height[right]:
                maxLeft = max(height[left], maxLeft)
                water += (maxLeft - height[left])
                left += 1
            else:
                maxRight = max(height[right], maxRight)
                water += (maxRight - height[right])
                right -= 1
            
        return water
                

