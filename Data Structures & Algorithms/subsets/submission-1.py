class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            print(i, "i before append")
            if i >= len(nums):
                print(subset, subset.copy())
                res.append(subset.copy())
                return 
            # print(res, "res")
            print(subset, "subset before append")
            subset.append(nums[i])
            dfs(i+1)
            print(i, "i  before pop")
            print(subset, "before pop")
            subset.pop()
            dfs(i+1)

        dfs(0)
        print(res, "line 21 res")
        return res