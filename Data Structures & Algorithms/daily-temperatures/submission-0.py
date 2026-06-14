class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp = []

        for i in range(len(temperatures)):
            while temp and (temperatures[temp[-1]] < temperatures[i]):
                x = temp.pop()
                result[x] = i - x

            temp.append(i)
            
        return result
        