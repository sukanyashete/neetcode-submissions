class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        total_left = (len(nums1) + len(nums2) + 1) // 2
        low, high = 0, len(nums1)
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = total_left - cut1
            
            # 2. Handle the boundaries with infinity
            left1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < len(nums1) else float('inf')
            
            left2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < len(nums2) else float('inf')
            
            # 3. Cross-Check Validation
            if left1 <= right2 and left2 <= right1:
                # Perfect cut found! Calculate median
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                    
            # 4. Adjust the binary search range
            elif left1 > right2:
                high = cut1 - 1  # Too many elements from nums1, move left
            else:
                low = cut1 + 1   # Too few elements from nums1, move right