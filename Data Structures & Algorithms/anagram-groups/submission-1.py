class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                ascii_index = ord(c) - ord("a")
                count[ascii_index]+=1
            lookup[tuple(count)].append(word)
        
        return list(lookup.values())