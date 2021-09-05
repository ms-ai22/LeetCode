class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        master = defaultdict(int)
        for num in nums1:
            master[num] -= 1
        for num in nums2:
            if num in master and master[num]<0:
                ans.append(num)
            master[num] += 1
        return ans
