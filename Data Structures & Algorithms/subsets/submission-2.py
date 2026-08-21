class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach
        # use backtracking to find all possible combinations
        # create a subsets lists for tracking all subsets we find, this is also our return value
        # we use i to keep track of our index, to make sure we are withing the boundary
        # run dfs that is called recursively(backtracking)
        subsets = []
        subset = []

        def dfs(i):
            # if index is out of bounds we have either found a subset or we need to return
            if i >= len(nums):
                # we copy here because without copy, we will append an update subset
                subsets.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)


        dfs(0)
        return subsets
