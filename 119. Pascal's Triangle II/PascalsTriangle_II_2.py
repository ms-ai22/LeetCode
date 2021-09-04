class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans.append(ans[i]*(rowIndex-i)//(i+1))
        return ans
