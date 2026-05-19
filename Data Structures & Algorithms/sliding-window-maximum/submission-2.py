class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for right in range(len(nums)):
            # Remove index that are out of the window of len k
            while dq and (dq[0] < (right-k+1)):
                dq.popleft()

            # Remove smaller elements from the back 
            # since we are trying to maintaining monotonous queue
            # queue in decreasing order of elements
            while dq and (nums[dq[-1]] < nums[right]):
                dq.pop()

            # Add the current index
            dq.append(right)

            # Append max once one window size is covered
            if right >= k-1:
                result.append(nums[dq[0]])

        return result 