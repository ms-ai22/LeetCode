class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for idx in range(len(s)-1,-1,-1):
            if s[idx] != " ":
                count += 1
            if count and s[idx]==" " or idx==0:
                return count
        return 1
