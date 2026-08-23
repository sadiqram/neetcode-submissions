class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            j=i
            while j< len(nums) and nums[j] == nums[i]:
                j+=1
            subset.pop()
            dfs(j)

        
        dfs(0)
        return subsets