class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(len(nums1)-1,-1,-1):
            if n==0:
                return
            elif nums2[n-1]>nums1[m-1] or m==0:
                nums1[idx] = nums2[n-1]
                n -= 1
            else:
                nums1[idx] = nums1[m-1]
                m -= 1
