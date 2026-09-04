class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def hr(nums):
            rob1,rob2 = 0,0

            for i in range(len(nums)):
                rob1,rob2 = rob2, max(nums[i] + rob1,rob2)
            return rob2
        
        return max(nums[0],hr(nums[1:]), hr(nums[:-1]))
        
       