class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        master = {}
        for idx,val in enumerate(nums):
            if target-val in master:
                return [idx,master[target-val]]
            master[val] = i
