class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for c in s:
            if c in freq:
                freq[c]+=1
            else:
                freq[c] = 1
            
        for c in t:
            if c not in freq or freq[c] <= 0:
                return False
            freq[c] -= 1
        
        return True

            

    
        