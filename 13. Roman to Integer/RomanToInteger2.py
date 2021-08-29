class Solution:
    def romanToInt(self, s: str) -> int:
        master = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        temp = 'I'
        for i in range(len(s)-1,-1,-1):
            if master[temp] > master[s[i]]:
                num -= master[s[i]]
            else:
                num += master[s[i]]
            temp = s[i]
        return num
