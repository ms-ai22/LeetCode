class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        while idx<len(nums)-1:
            if nums[idx]==nums[idx+1]:
                del nums[idx+1]
            if idx+1==len(nums):
                return idx+1
            if nums[idx]<nums[idx+1]:
                idx += 1
        return idx+1
