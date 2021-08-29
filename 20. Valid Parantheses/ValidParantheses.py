class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(brackets[i])
            elif not stack or i!=stack[-1]:
                return False
            elif i==stack[-1]:
                stack.pop()
        return not stack
