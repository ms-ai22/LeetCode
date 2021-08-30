class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if val!=num:
                nums[idx] = num
                idx += 1
        return idx
