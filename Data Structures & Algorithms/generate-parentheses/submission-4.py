class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_count, closed_count, curr):
            if closed_count == n:
                res.append("".join(curr))

            #  if valid open
            if open_count < n:
                curr.append("(")
                dfs(open_count + 1, closed_count, curr)
                curr.pop()


            # if valid close
            if (open_count - closed_count) >= 1:
                curr.append(")")
                dfs(open_count, closed_count + 1, curr)
                curr.pop()


        dfs(0,0,[])
        return res
            
        