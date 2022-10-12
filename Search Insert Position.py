# Binary Search with Lower Bound O(log n)
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low