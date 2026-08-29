class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1]* len(nums)

        for i in range(1,len(nums)):
            subproblems = [res[k] for k in range(i) if nums[k] < nums[i]]
            res[i] = 1 + max(subproblems,default=0)
        
        return max(res,default=0)
        