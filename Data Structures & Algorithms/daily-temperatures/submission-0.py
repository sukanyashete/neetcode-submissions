class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # this is the result array
        result = [0] * len(temperatures)
        # this is monotonic decreasing stack storing indices
        temp = []

        for i in range(len(temperatures)):
            # While the stack isn't empty AND today's temp is warmer
            # than the temp at the index on top of the stack
            while temp and (temperatures[temp[-1]] < temperatures[i]):
                x = temp.pop()
                result[x] = i - x

            # Today's index always gets added to the stack to wait for its warmer day
            temp.append(i)
            
        return result
    
