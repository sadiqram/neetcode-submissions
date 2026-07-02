class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t) or len(s) < 1:
            return False
        tracker = {}

        for c in s:
            if c in tracker:
                tracker[c]+=1
            else:
                tracker[c] = 1
        
        for c in t:
            if not c in tracker:
                return False
            tracker[c]-=1
            if tracker[c] < 0:
                return False
        return True
