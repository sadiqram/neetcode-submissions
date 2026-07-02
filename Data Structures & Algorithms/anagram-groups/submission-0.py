class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = defaultdict(list)
        # find word signature, use sig as tuple key -> [values]

        
        

        # store each char as acii and use as index in sigs

        for word in strs:
            sigs= [0 ]* 26
            for char in word:
                sigs[ord(char) - ord("a")]+=1
            lookup[tuple(sigs)].append(word)
        
        return list(lookup.values())

        