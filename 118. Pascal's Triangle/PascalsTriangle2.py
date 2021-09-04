class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            ans.append([1]+[a+b for a,b in zip(ans[-1],ans[-1][1:])]+[1])
        return ans
