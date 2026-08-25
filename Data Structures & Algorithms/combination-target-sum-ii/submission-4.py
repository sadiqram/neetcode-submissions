class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])

            curr.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j+=1
            dfs(j, curr, total)
        
        dfs(0,[],0)
        return res
