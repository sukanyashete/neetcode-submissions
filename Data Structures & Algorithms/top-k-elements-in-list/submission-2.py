class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        ccounts = {}
        result = []

        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        for i,j in counts.items():
            if j in ccounts:
                ccounts[j].append(i)
            else:
                ccounts[j] = [i]

        for i in range(len(nums), 0, -1):
            if i in ccounts:
                result.extend(ccounts[i])
            if len(result) >= k:
                break

        return result[:k]
            