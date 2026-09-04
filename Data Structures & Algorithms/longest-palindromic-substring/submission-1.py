class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach check if each index is a palindrom, the index is seen as the center of that palindrome
        res = ""
        
        def valid_pal(l,r):
            nonlocal res
            while l >= 0 and r < len(s)  and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            

        for i in range(len(s)):
            # odd length
            l,r = i, i
            # if is valid palindrome basically
            valid_pal(l,r)


            # Even length
            l,r = i, i + 1
            # if is valid palindrome basically
            valid_pal(l,r)
        return res

        