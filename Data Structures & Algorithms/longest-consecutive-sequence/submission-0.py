class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0


        for n in nums:
            # if is a start of sequence
            if (n-1) not in lookup:
                length = 0
                while  (n + length) in lookup:
                    length +=1
                longest = max(length, longest)
        return longest
        

            
       
