class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        while len(ans[-1])<numRows:
            temp = []
            for idx in range(1,len(ans[-1])):
                temp.append(ans[-1][idx-1]+ans[-1][idx])
            ans.append([1]+temp+[1])
        return ans
