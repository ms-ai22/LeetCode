class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1,rowIndex+1):
            ans.append([1]+[a+b for a,b in zip(ans[-1],ans[-1][1:])]+[1])
        return ans[rowIndex]
