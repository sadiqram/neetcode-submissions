class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        
        def is_pal(l,r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            

        for i in range(len(s)):
            # Odd length strings
            l,r = i,i 
            is_pal(l,r)
               

            # Even length string
            l,r = i, i + 1
            is_pal(l,r)
                

        return count
        