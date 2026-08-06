class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lookup = set()
        for n in nums:
            if n in lookup:
                return True
            lookup.add(n)
        return False
        