class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            # Take
            subset.append(nums[i])
            dfs(i+1)
            # Skip
            subset.pop()
            dfs(i+1)

        dfs(0)
        return subsets

        