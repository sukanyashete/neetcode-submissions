class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        for i in strs:
            s = str(sorted(i))
            if s in groups:
                groups[s].append(i)
            else:
                groups[s] = [i]
        #print(groups)
        for i in groups.values():
            result.append(i)
        #print(result)

        return result