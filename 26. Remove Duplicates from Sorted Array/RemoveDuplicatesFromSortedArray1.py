class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for num in nums:
            if num != nums[idx-1]:
                nums[idx] = num
                idx += 1
        return idx
