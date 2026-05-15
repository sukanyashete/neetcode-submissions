class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxf = 0
        l = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            #win = right - left + 1
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
                #win -= 1
            
            l = max(l, right-left+1)
        
        return l
