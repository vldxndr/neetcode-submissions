from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else :
                if not stack:
                    return False
                if c == ')' and stack.pop() == '(':
                    continue
                elif c == ']' and stack.pop() == '[':
                    continue
                elif c == '}' and stack.pop() == '{':
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False