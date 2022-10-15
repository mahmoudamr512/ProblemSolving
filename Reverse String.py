# Question Link: https://leetcode.com/problems/reverse-string/?envType=study-plan&id=algorithm-i

def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s) - 1

    while (start <= end):
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    print(s)

reverseString(["h","e","l","l","o"])