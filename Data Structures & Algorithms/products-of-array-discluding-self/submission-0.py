class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            ltor = [1] * len(nums)
            rtol = [1] * len(nums)
            result = [1]*len(nums)
            ltor[1] = nums[0]
            rtol[len(nums)-2] = nums[len(nums)-1] # last element in arr nums

            for i in range(2, len(nums)):
                ltor[i] = nums[i-1] * ltor[i-1]
            print("ltor is ", ltor)
            for j in range(len(nums)-3, -1, -1):
                rtol[j] = nums[j+1] * rtol[j+1]
            print("rtol is ", rtol)        
            for i in range(0, len(nums)):
                result[i] = ltor[i] * rtol[i]

            return result

