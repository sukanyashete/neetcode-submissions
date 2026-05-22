class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initial edge case check: if t is longer than s, it's impossible to find a window
        if (len(t) > len(s)) or (not s) or (not t):
            return ""

        # Frequency map for characters we are looking for in 't'
        dict_t = Counter(t)
        
        # 'required' is the number of unique characters in 't' that must reach a certain frequency
        required = len(dict_t)
        
        # Window pointers and state tracking
        l, r = 0, 0
        formed = 0  # Tracks how many unique characters in 't' have met their frequency requirement in the current window
        window_counts = {} # Tracks frequencies of characters in the current window [l, r]
        
        # Stores the result as (window_length, left_index, right_index)
        ans = float("inf"), None, None

        while r < len(s):
            # EXPAND: Add character from the right to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character's frequency matches its required frequency in 't', 
            # we've satisfied the requirement for this unique character.
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # CONTRACT: While the window is valid (contains all chars of 't' in required amounts),
            # try to shrink it from the left to find a smaller valid window.
            while l <= r and formed == required:
                char = s[l]

                # Update the global minimum window result
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # Remove the character at the left pointer from the window state
                window_counts[char] -= 1
                
                # If removing this character makes the window invalid (frequency drops below requirement),
                # decrement the 'formed' counter.
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                # Move left pointer forward to keep looking for smaller windows
                l += 1    

            # Move right pointer forward to continue expanding
            r += 1    
            
        # Return the substring if a valid window was found, otherwise return empty string
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# The formed variable: This is the "brain" of the algorithm. It allows us to avoid checking the entire dictionary in every loop. We only care when a character count exactly hits the target (increment) or falls below the target (decrement).
# The while formed == required loop: This represents the "tightening" phase. It ensures that once we find a valid window, we immediately discard unnecessary characters from the left to get the minimum possible size.
