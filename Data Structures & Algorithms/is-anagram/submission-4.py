class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}

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

        if dictt == dicts:
            return True
        else: 
            return False