#Question Link: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
            else:
                try:
                    if letter == ")" and stack[-1] == "(":
                        stack.pop()
                    elif letter == "}" and stack[-1] == "{":
                        stack.pop()
                    elif letter == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
s = Solution()
print(s.isValid("]"))