class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:

        i = 0

        decoded = []
        while i < len(s):
            wordlen = ""
            while s[i]!= "#":
                wordlen += s[i]
                i+=1

            decoded.append(s[i + 1: i + int(wordlen) + 1])
            i+= int(wordlen) + 1
        return decoded
    
            



