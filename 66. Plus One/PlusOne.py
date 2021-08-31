class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        temp = 0
        for digit in digits:
            temp = 10*temp + digit
        temp += 1
        for char in str(temp):
            ans.append(int(char))
        return ans
