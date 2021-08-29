class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = ""
        ans = ''
        j = -1
        while True:
            j += 1
            try:
                temp = strs[0][j]
            except:
                return ans
            for i in strs:
                if not i[j:].startswith(temp):
                    return ans
            ans += temp
