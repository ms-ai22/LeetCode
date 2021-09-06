class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        lo = 0
        hi = len(s)-1
        while hi >= lo:
            if not s[lo].isalnum():
                lo += 1
            if not s[hi].isalnum():
                hi -= 1
            if s[lo].isalnum() and s[hi].isalnum():
                if s[lo].lower() == s[hi].lower():
                    lo += 1
                    hi -= 1
                else:
                    return False
        return True
