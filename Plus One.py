# Question Link: https://leetcode.com/problems/plus-one/

# Naive Easy Solution lol
class Solution:
    def plusOne(self, digits):
        digits = [str(digit) for digit in digits]
        number = int("".join(digits))
        return list(str(number+1))

