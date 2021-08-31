class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxima = float('-inf')
        local_maxima = 0
        for num in nums:
            local_maxima += num
            maxima = max(num, local_maxima, maxima)
            if local_maxima<num:
                local_maxima = num
        return maxima
