class Solution:
    def romanToInt(self, s: str) -> int:
        master = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        temp = 0
        for i in s:
            if (temp==1 and (i=='V' or i=='X')) or (temp==10 and (i=='L' or i=='C')) or (temp==100 and (i=='D' or i=='M')):
                num -= 2*temp
            temp = master[i]
            num += temp    
        return num
