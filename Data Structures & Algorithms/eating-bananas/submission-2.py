class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(n):
            total = 0
            for i in piles:
                total += (i + n - 1) // n  #ceil division
            return total

        # Search space is how many bananas can be had in an hour
        # max no. of bananas can be eaten at a time is max value in piles
        # min no. of bananas can be eaten at a time is 1
        # returning left because left is the min integer.
        # anything after left will definetely satify this condition;
        # but left is the least required. 
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
