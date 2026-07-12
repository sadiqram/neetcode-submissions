class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach
        # convert nums into set
        lookup = set(nums)
        max_len = 0

        for num in nums:
            curr_len = 0
            if num - 1 not in lookup:
                curr_len += 1
                while num + curr_len in lookup :
                    curr_len+=1
            max_len = max(max_len, curr_len)

        return max_len

            
        