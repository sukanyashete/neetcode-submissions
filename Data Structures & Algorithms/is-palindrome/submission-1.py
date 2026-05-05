class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while (i < j) and (not str.isalnum(s[i])):
                i += 1
            while (j > i) and (not str.isalnum(s[j])):
                j -= 1
        
            if str.lower(s[i]) != str.lower(s[j]):
                print("False, s[i] is %c and s[j] is %c", s[i], s[j])
                return False
            i += 1
            j -= 1
        return True
            
