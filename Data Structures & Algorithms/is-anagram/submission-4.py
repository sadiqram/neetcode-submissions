class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = { char:0 for char in s}
        t_map = { char:0 for char in t }
        if len(s)!= len(t):
            return False

        for char in s:
            s_map[char]+=1
        for char in t:
            t_map[char]+=1
        
        for char in t:
            if char not in s_map or s_map[char]!=t_map[char]:
                return False
        return True