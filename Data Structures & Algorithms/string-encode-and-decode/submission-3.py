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
            count = ""
            while s[i] != "#":
                count+=s[i]
                i+=1
            decoded.append(s[i+1 : i +int(count) + 1 ])
            i += (int(count) + 1)

        return decoded
