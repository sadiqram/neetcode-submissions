class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        prev1, prev2 = 1,1

        for i in range(1,len(s)):
            curr = 0
            
            if  1 <= int(s[i]) <= 9:
                curr += prev1

            if 10 <= int(s[i-1: i + 1]) <= 26:
                curr += prev2

            if curr == 0:
                return 0

            prev1,prev2 = curr, prev1

        return prev1

            


            

        

        