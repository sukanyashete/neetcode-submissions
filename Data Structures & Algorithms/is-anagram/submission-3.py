class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}

        if len(s) != len(t):
            return False
            
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        for i in t:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1

        for i in dicts:
            if i not in dictt:
                return False
            else:
                if dicts[i] != dictt[i]:
                    return False
        
        return True