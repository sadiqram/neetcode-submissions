class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        l = 1
        r = len(heights)

        while l < r:
            w = r - l
            h = min(heights[l-1], heights[r-1])
            a = w*h
            curr_max = max(a,curr_max)
            if heights[l-1] < heights[r-1]:
                l+=1
            elif heights[r-1] < heights[l-1]:
                r-=1
            else:
                l+=1

        return curr_max


        