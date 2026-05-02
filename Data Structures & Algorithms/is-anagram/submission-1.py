class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1

        for i in dict1.keys():
            if i in dict2.keys():
                if dict1[i] != dict2[i]:
                    return False
            else:
                return False

        return True 

           