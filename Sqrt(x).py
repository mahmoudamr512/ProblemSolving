# Question Link: https://leetcode.com/problems/sqrtx/

# Can't use Sqrt(x) or power 0.5

#Naiive - O(sqrt(n)) solution

# def mySqrt(self, x: int) -> int:
#     for i in range(0, x + 1):
#         if i * i > x:
#             return i - 1
#         elif i * i == x:
#             return i
#     return 0

#O(log(n)) - Binary Search Solution

def mySqrt(self, x: int) -> int:
    low = 0
    high = x

    while low <= high:
        mid = (low+high)//2

        if mid * mid == x or (mid*mid < x and (mid+1)*(mid+1) > x):
            return mid
        elif mid*mid < x:
            low = mid + 1
        else:
            high = mid -1

