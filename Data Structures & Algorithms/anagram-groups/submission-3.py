class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                index = ord(c) - ord("a")
                count[index]+=1
            lookup[tuple(count)].append(word)
        return list(lookup.values())
        