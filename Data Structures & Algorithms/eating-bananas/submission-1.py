class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(n):
            total = 0
            for i in piles:
                total += (i + n - 1) // n  #ceil division
            return total

        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            needed_hrs = hours_needed(mid)
            if needed_hrs > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left