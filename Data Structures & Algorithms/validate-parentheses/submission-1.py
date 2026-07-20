from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"]":"[",")":"(","}":"{"}
        stack = deque()
        if len(s)<=1:
            return False
        
        for c in s:
            # we only start popping when we reach a closing(parentheses)
            if c in lookup:
                if stack and stack[-1]==lookup[c]:
                    stack.pop()
                else:
                    return False
            else:
                # if not in lookup c is an opening
                stack.append(c)
                
            
            
        return False if stack else True
        