from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")":"(", "]":"[","}":"{"}
        stack = deque()

        for c in s:
            if c in lookup:
                if stack and stack[-1] == lookup[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
        