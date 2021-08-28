class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        num = 0
        if neg:
            x *= -1
        while x > 0:
            q,r =  divmod(x,10)
            num = num*10 + r
            x = q
        if neg:
            num *= -1
        if -(2**31)<=num<=(2**31)+1:
            return num
        return 0