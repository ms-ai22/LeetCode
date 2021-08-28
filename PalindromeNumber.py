class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            q,r =  divmod(temp,10)
            rev = rev*10 + r
            temp = q
        return rev==x
