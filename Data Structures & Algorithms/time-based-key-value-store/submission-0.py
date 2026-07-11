class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []

        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        pairs = self.timemap[key]
        l = 0
        r = len(pairs) - 1
        result = ""

        while l <= r:
            mid = (l+r)//2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result
            
