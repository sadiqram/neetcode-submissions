class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = { char:0 for char in s}
        t_map = { char:0 for char in t }

        for char in s:
            s_map[char]+=1
        for char in t:
            t_map[char]+=1
        
        # for char in t:
        #     res = s_map.get(char,"0")
            
        #     if t_map[char]!= res:
        #         return False
        return s_map == t_map