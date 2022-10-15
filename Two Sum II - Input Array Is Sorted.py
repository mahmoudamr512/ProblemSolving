# Question Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer Solution O(N)

        start = 0
        end = len(numbers) - 1
        indices = []

        while (start <= end):
            sum = numbers[start] + numbers[end]

            if sum == target:
                indices.append(start + 1)
                indices.append(end + 1)
                break
            elif sum < target:
                start += 1
            else:
                end -= 1

        return indices