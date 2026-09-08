class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  use two pointers l and r to iterate input
        #  compare input at l and r, if not the same return False

        def isAlphanum(c):
            return (("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9"))
        l = 0
        r = len(s) - 1
        lower = s.lower()
        while l <= r:
            while  l <= r  and not isAlphanum(lower[l]) :
                l+=1
            while l <= r and not isAlphanum(lower[r]):
                r-=1
            if l >  r:
                break
            if lower[l] != lower[r]:
                return False
            l+=1
            r-=1
        return True
        