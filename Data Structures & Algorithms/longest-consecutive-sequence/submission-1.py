class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        maxlen = 0
        for i in new:
            length = 1
            if (i-1) not in new:
                #length = 1
                while i+length in new:
                    length += 1
            maxlen = max(maxlen, length)

        return maxlen
