class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        maxlen = 0
        seen = set()

        if s:
            seen = set(s[0])

        if len(s) <= 1:
            return len(s)

        else:
            for right in range(1, len(s)):
                if s[right] in seen:
                    maxlen = max(maxlen, right - left)
                    while s[right] in seen:
                        seen.remove(s[left])
                        left += 1
                    seen.add(s[right])
                else:
                    seen.add(s[right])
        
            return max(maxlen, len(seen))

