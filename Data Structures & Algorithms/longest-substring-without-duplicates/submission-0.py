class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = l + 1
        max_len = 0
        lookup = set(s[l])



        while r < len(s):
          
            while s[r] in lookup:
                lookup.remove(s[l])
                l+=1
            lookup.add(s[r])
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len
            
                

            