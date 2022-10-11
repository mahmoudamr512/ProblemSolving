import re
# First Solution comes to my mind, BruteForce. O(N*M) where N is the length of the smallest string and M is the number of strings
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        target_string = min(strs, key=len)
        prefix = ""

        for j in range(0, len(target_string)):

            if j == 0:
                comp_string = target_string[0]
            elif j == len(target_string)-1:
                comp_string = target_string
            else:
                comp_string = target_string[0:j+1]

            if all(re.match(rf'^{comp_string}', string) is not None for string in strs):
                prefix = comp_string if len(comp_string) > len(prefix) else prefix
            else:
                break

        return prefix

s = Solution()
print(s.longestCommonPrefix(["abab","aba","abc"]))