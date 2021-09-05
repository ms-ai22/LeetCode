class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        master = defaultdict(int)
        n1,n2 = len(nums1),len(nums2)
        for idx in range(max(n1,n2)):
            if idx<n1:
                if nums1[idx] in master and master[nums1[idx]]>0:
                    ans.append(nums1[idx])
                master[nums1[idx]] -= 1
            if idx<n2:
                if nums2[idx] in master and master[nums2[idx]]<0:
                    ans.append(nums2[idx])
                master[nums2[idx]] += 1
        return ans
