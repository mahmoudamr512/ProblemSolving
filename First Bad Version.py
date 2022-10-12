#Question Link: https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         low = 1
#         high = n
#         mid = 0
#
#         while (low <= high):
#             mid = (low + high) // 2
#
#             if not isBadVersion(mid):
#                 low = mid + 1
#             else:
#                 if not isBadVersion(mid - 1):
#                     return mid
#                 high = mid - 1
#
#         return mid