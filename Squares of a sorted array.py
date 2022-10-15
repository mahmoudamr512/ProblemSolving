class Solution:
    # While the obvious solutions are going to be using the sorted array, those
    # solutions are O(nlogn) in time complexity.
    # However, we want to go for O(n) solutions, using two pointers
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return_arr = [0] * len(nums)

        write_pointer = len(nums) - 1
        left_pointer = 0
        right_pointer = len(nums) - 1

        while write_pointer >= 0:
            right_sq = nums[right_pointer] ** 2
            left_sq = nums[left_pointer] ** 2
            print(right_sq)
            print(left_sq)
            if left_sq > right_sq:
                return_arr[write_pointer] = left_sq
                left_pointer += 1
            else:
                return_arr[write_pointer] = right_sq
                right_pointer -= 1
            write_pointer -= 1

        return return_arr
