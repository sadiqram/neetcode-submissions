class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr,openn, closed):
            # if finished
            if  closed == n:
                res.append("".join(curr))
                return

            #  if can open
            if openn < n:
                curr.append("(")
                dfs(curr, openn + 1,closed)
                curr.pop()

            # if can close
            if closed < n and openn - closed > 0:
                curr.append(")")
                dfs(curr,openn, closed + 1)
                curr.pop()

        dfs([],0,0)
        return res

        