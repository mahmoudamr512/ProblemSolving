#Link to question: https://leetcode.com/problems/roman-to-integer/

# First Solution comes to my mind O(N) where N is the length of the string
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        lettersToNumbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i, l in enumerate(s):
            if i != len(s) - 1:
                if lettersToNumbers[l] >= lettersToNumbers[s[i + 1]]:
                    sum += lettersToNumbers[l]
                else:
                    sum -= lettersToNumbers[l]
            else:
               sum += lettersToNumbers[l]

        return sum