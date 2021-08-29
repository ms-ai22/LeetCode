class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = 0
        temp = x
        while temp > 0:
            q,r =  divmod(temp,10)
            num = num*10 + r
            temp = q
        return num==x
