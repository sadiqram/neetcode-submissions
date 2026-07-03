class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # use ascii to represent anagrams
        #  each anagram gets a list, which contains alphabets at each idx
        # The count for each letter creates a unique id, which we can also use as a key in our map
        res = defaultdict(list)
        for ana in strs:
            uid = [0] * 26
            for char in ana:
                idx = ord(char) - ord("a")
                uid[idx] += 1
            res[tuple(uid)].append(ana)
        return list(res.values())
            

                