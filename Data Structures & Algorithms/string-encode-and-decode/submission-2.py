class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i+=1
            decoded.append(s[i+1: i + int(length)+1])
            i+= int(length) + 1
        return decoded
