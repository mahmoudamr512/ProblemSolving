class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
                # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
s = Solution()
s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)