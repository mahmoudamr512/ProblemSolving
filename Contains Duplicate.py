#Question Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums) -> bool:

        nums_hash = {}

        for num in nums:
            nums_hash.setdefault(num, 0)
            nums_hash[num] += 1

            if nums_hash[num] == 2:
                return True

        return False