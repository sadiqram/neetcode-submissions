class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i,curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for num in nums:
                if num not in used:
                    used.add(num)
                    curr.append(num)
                    dfs(i,curr,used)
                    curr.pop()
                    used.remove(num)

        
        dfs(0,[],set())
        return res

        

        