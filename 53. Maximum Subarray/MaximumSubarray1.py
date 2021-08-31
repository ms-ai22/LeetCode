class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxima = float('-inf')
        local_maxima = 0
        for num in nums:
            local_maxima += num
            if local_maxima > maxima:
                maxima = local_maxima
            if local_maxima<0:
                local_maxima = 0
        return maxima
