class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        temp = []
        for i in s:
            if i in '([{':
                temp.append(brackets[i])
            elif not temp or i!=temp[-1]:
                return False
            elif i==temp[-1]:
                temp.pop()
        return not temp
