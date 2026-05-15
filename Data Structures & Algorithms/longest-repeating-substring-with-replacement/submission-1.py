class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        maxlen = 0
        max_freq = 0
        freq = defaultdict(int)
        
        for right in range(len(s)):
            # include current char in window
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            
            # current window size
            window_size = right - left + 1
            
            # replacements needed = non-max chars in window
            if window_size - max_freq > k:
                # shrink from left
                freq[s[left]] -= 1
                left += 1
                window_size = right - left + 1  # optional, since maxlen uses this implicitly
            
            maxlen = max(maxlen, window_size)
        
        return maxlen
