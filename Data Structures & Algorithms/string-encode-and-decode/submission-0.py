class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            delimiter = str(len(word)) + "#"
            delimiter += word
            encoded_str+= delimiter
        return encoded_str

    def decode(self, s: str) -> List[str]:

        i = 0
        decoded_lst = []
        
        

        while i < len(s):
            j = i

            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            word = str(s[j+1 : j+1+length])
            decoded_lst.append(word)
            i = j + 1 + length
        return decoded_lst

