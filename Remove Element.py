#Question Link: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
