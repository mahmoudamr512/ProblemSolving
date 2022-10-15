# First Appraoch I thought of is O(N*M)
# Solution isn't effecient because everytime you have to check the element in all elements of
# Second array
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         smaller = None
#         larger = None
#         indices = []

#         if len(nums1) < len(nums2):
#             smaller = nums1
#             larger = nums2
#         else:
#             smaller = nums2
#             larger = nums1

#         for i in smaller:
#             if i in larger:
#                 larger.remove(i)
#                 indices.append(i)
#         return indices

# Next, let's think of an optmized way that takes a single traversal through each loop and returning the indices with O(N+M) as time and O(N) as space.
# Remember Dictionary Lookup in python is O(1)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = []

        d = {}
        smaller = None
        larger = None
        indices = []

        if len(nums1) < len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1

        for i in larger:
            d.setdefault(i, 0)
            d[i] += 1

        for j in smaller:
            if j in d:
                if d[j] >= 1:
                    indices.append(j)
                    d[j] -= 1

        return indices