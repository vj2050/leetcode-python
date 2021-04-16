# Fibonacci approach :
class Solution:
    def climbStairs(self, n):
        first = 1  # fibonacci series starting from 1
        second = 2

        if n == 1:
            return first

        for i in range(3, n + 1):
            third = 0
            third = first + second

            first = second
            second = third

        return second  # since when n=2 , doesnt enter for loop and directly return second value, for n>2, second = third in for loop till last iteration hence safe to return "second" everytime

obj = Solution()
print(obj.climbStairs(3))