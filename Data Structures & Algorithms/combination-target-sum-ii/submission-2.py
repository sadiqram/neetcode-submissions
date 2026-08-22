class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # Take
            # if total + candidates[i] <= target:
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()



            #  Skip
            # if we skip a num we need to make sure we don't re select a dupe later down the tree
            
            # curr.pop()
            j=i
            while j<= len(candidates) - 1 and candidates[j] == candidates[i]:
                j+=1
                
            dfs(j,curr, total)
        
        dfs(0,[],0)
        return res

        