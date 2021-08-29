class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans.append(i[0])
            else:
                break
        return "".join(ans)
