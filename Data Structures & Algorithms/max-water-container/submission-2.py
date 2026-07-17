class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        l = 0
        r = len(heights)-1

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w*h
            curr_max = max(a,curr_max)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return curr_max


        