class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t) or len(s) < 1:
            return False
        lookup = {}

        for c in s:
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1
        
        for c in t:
            if c not in lookup:
                return False
            lookup[c]-=1
            if lookup[c]< 0:
                return False
        return True
        