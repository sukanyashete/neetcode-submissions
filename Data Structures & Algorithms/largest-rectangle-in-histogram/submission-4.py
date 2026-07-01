class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        stk.append((heights[0], 0)) #[height, index]

        for i in range(1, len(heights)):
            if heights[i] >= stk[-1][0]:
                stk.append((heights[i], i))
            else: 
                idx = i
                while stk and (stk[-1][0] > heights[i]):
                    a = (i - stk[-1][1]) * stk[-1][0] # area = width * height
                    max_area = max(max_area, a)
                    prev_height, prev_idx = stk.pop()
                    idx = prev_idx
                stk.append((heights[i], idx))

        # The remaining bars extend all the way to the end of the histogram
        end_index = len(heights)
        while stk:
            a = (end_index - stk[-1][1]) * stk[-1][0]
            max_area = max(max_area, a)
            stk.pop()   

        return max_area

            