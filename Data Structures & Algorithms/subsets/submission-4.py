class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        

        def dfs(i,curr):
            # base case
            if i >= len(nums):
                res.append(curr.copy())
                return    

            # take
            curr.append(nums[i])
            dfs(i+1,curr)

            # skip
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0,[])
        return res
        