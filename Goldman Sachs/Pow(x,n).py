class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n < 0:
            x = 1 / x
            n = -n  # converting to positive power

        ans = 1
        currentProduct = x
        while (n > 0):  # while power is positive, keep running
            if n % 2 == 1:  # power is odd, so add the odd one, x to the ans and keep
                ans = ans * currentProduct

            currentProduct = currentProduct * currentProduct
            n = n // 2  # java does not support this python feature of only taking integer part of quotient
        return ans

obj = Solution()
print(obj.myPow(2,5))