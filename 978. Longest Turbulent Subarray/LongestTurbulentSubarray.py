class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count = 1
        ans = 1
        inc = None
        for idx in range(len(arr)-1):
            if (not inc and arr[idx]<arr[idx+1]) or (inc and arr[idx]>arr[idx+1]):
                count += 1
            else:
                ans = max(count, ans)
                count = 2 if arr[idx]!=arr[idx+1] else 1
            inc = arr[idx] < arr[idx+1]
        return max(ans,count)
