# First Solution that I thought of is to sort and use two pointers, however, this will change the index.

# Change to Hashmap
class Solution:
    def twoSum(self, nums, target: int):
        hashmap = {}

        for index, value in enumerate(nums):
            complementary = target - value

            if complementary in hashmap: return [hashmap[complementary], index]
            hashmap[value] = index

s = Solution()
s.twoSum([2,7,11,15], 9)