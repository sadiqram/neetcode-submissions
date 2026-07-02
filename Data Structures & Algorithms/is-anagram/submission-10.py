class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tracker = {}
        for char in s:
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1
        for char in t:
            if char not in tracker or tracker[char] <= 0:
                return False
            tracker[char] -= 1
        return True

        