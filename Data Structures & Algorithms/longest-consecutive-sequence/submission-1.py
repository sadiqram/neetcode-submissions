class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lookup = set(nums)

        for num in nums:
            if (num -1) not in lookup:
                curr_len = 0
                while (num + curr_len) in lookup:
                    curr_len+=1
                longest = max(curr_len,longest)
        return longest

