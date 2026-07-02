class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        # 1. Binary search to find the correct row
        top = 0
        bot = rows - 1
        row = -1

        while top <= bot:
            mid = top + (bot - top) // 2
            
            if target > matrix[mid][cols - 1]:
                top = mid + 1      # Target is in a lower row
            elif target < matrix[mid][0]:
                bot = mid - 1      # Target is in an upper row
            else:
                row = mid          # Found the correct row!
                break
        
        # If the row pointers crossed and we didn't break, target isn't here
        if row == -1:
            return False

        low = 0
        high = cols - 1

        # 2. Binary search within the identified row
        while low <= high:
            midcurr = int(low + ((high-low)/2))
            if target < matrix[mid][midcurr]:
                high = midcurr -1
            elif target > matrix[mid][midcurr]:
                low = midcurr + 1
            elif target == matrix[mid][midcurr]:
                return True

        return False
