class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for idx,char in enumerate(haystack):
            if char==needle[0] and haystack[idx:idx+len(needle)]==needle:
                return idx
        return -1
