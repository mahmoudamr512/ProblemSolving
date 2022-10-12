#Question Link: https://leetcode.com/problems/maximum-subarray/

# Brute Force Solution - O(N^2) - Time Limit Exceeded

# class Solution:
#     def maxSubArray(self, nums) -> int:
#
#         max = -999
#         for i,num in enumerate(nums):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) >= max:
#                     max = sum(nums[i:j+1])
#
#         return max

# Sliding Window Solution O(N)
class Solution:
    def maxSubArray(self, nums) -> int:

        maxSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0

            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum

s = Solution()
print(s.maxSubArray([5,4,-1,7,8]))