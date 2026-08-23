class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr,open_count, close_count):
            # if finsihed
            if close_count == n:
                res.append("".join(curr))
                return 

            # if valid open
            if open_count < n:
                curr.append("(")
                dfs(curr,open_count + 1, close_count)
                curr.pop()

            # if valid close
            if open_count - close_count > 0: # needs to be atleast 1 open ( for close to be eligible/valid
                curr.append(")")
                dfs(curr, open_count, close_count + 1)
                curr.pop()
            
        dfs([],0,0)
        return res