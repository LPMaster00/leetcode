class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        A = m - 1
        B = n - 1
        C = m + n - 1
        while A >= 0 and B >= 0:
            if (nums1[A] < nums2[B]):
                nums1[C] = nums2[B]
                B -= 1
            else:
                nums1[C] = nums1[A]
                A -= 1
            C -= 1
            
        while B >= 0:
            nums1[C] = nums2[B]
            B -= 1
            C -= 1
