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
        

# dictionary count maintains freq count of elements in the dictionary. format is { element1: no. of times it appears in array nums(frequency), element2: frequency}
# dictionary ccount is the actual bucket. Maintains count of frequncies. Means maintains a bucket of elements having the same frequncy count. eg: Assume this to #     be the dictionary ccount {2:[1,3,5], 4:[6]}. key = frequncy values: elements in array num with its frequcny as key stored as list.
#     Here it means elements 1, 3 and 5 are there 2 times in the array nums(its frequncy count) and among the no.s with frequcny 4 there is only number 6. 

# Time Complexity: O(n)

# Why did we use range(len(nums), 0, -1) instead of range(max(ccounts.keys()), 0, -1) in line 16 ?
# Ans: Max possible frequency of any element = n (array size) since there are chances when all the elements in the array is the same element.
#      eg. think of this array [1,1,1,1] where n=4. counts = {1:4}, ccounts={4:1}
#      Computing max() in terms of time complexity costs O(n) time.
#      len(nums) → O(1) to compute, max(ccounts.keys()) → O(n) to compute.
#      Both are valid upper bounds since max frequency ≤ n. Why pay O(n) extra when O(1) gives you the same correct upper bound. So len() was chosen.
            
