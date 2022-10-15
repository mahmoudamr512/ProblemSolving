# Question Link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # Base Case Handling is array of 1 element, just return it

    start, end = 0, 1

    while (end < len(nums)):
        if nums[start] == 0 and nums[end] == 0:
            end += 1
            continue
        elif nums[start] == 0 and nums[end] != 0:
            nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end += 1

moveZeroes([0,1,0,3,12])