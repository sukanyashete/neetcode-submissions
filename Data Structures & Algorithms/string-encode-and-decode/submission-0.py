class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs:
            en += (str(len(i)) + "#" + i)

        #print(en)
        return en

    def decode(self, s: str) -> List[str]:
        de = []
        leng = ""
        j = 0
        i = 0
        while i < len(s):
            word = ""
            while s[j] != "#":
                leng += s[j]
                j += 1
            l = int(leng)
            j += 1
            while l > 0:
                word += s[j]
                j += 1
                l -= 1
            de.append(word)
            i = j
            leng = ""
        #print("de = ", de)
        return de
