class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if (len(s1) > len(s2)):
            return False

        cnt_s1 = [0] * 26
        cnt_s2 = [0] * 26
        k = len(s1)

        for i in s1:
            cnt_s1[ord(i) - ord('a')] += 1
        for i in range(k):
            cnt_s2[ord(s2[i]) - ord('a')] += 1

        if cnt_s1 == cnt_s2:
            return True
        else:
            for j in range(k, len(s2)):
                cnt_s2[ord(s2[j]) - ord('a')] += 1
                cnt_s2[ord(s2[j-k]) - ord('a')] -= 1

                if cnt_s2 == cnt_s1:
                    return True
        
        return False


# Sliding window fixed sized.
# ord(letter) - ord('a') is done to fit in alphabetical range from 0 to 25 in an array. (a=0, b=1, c=2,.... )
# ord(letter) : this function gives the ascii value of that letter. 
# the opposite of this function is chr(letter). Converts the number to letter.
# chr(num + ord('a')) : Applicable to this case will convert number in range 0-25 to its equivalent a-z.
