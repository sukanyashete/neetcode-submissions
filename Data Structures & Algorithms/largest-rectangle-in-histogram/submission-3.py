class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        stk.append((heights[0],0)) #[height, index]
        i = 0
        k = (0,0)

        for i in range(1, len(heights)):
            if heights[i] >= stk[-1][0]:
                stk.append((heights[i], i))
            else:
                while stk and (stk[-1][0] > heights[i]):
                    a = (i - stk[-1][1]) * stk[-1][0]
                    max_area = max(max_area, a)
                    k = stk.pop()
                stk.append((heights[i],k[1]))
        
        i +=1
        while stk:
                a = (i - stk[-1][1]) * stk[-1][0]
                max_area = max(max_area, a)
                stk.pop()   

        return max_area        