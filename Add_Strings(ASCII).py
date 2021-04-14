class Solution:
    def addStrings(self, num1, num2):
        ptr1, ptr2 = len(num1) - 1, len(num2) - 1  # pointers starting from unit's place
        carry, summ, result = 0, 0, []

        while (ptr1 >= 0 or ptr2 >= 0):
            a = ord(num1[ptr1]) - ord('0') if ptr1 >= 0 else 0
            # ord : ASCII equivalent of strings 0-9 is 48-57. Retreive actual integer values from strings by subtrating ASCII equiv from ASCII 0 (eg. for int 1, ASCII equiv 49 - ASCII equiv 48 = 1)

            b = ord(num2[ptr2]) - ord('0') if ptr2 >= 0 else 0

            summ = (a + b + carry) % 10  # takes last digit only and carry forwards the rest
            carry = (a + b + carry) // 10  # first digit only as carry
            result.append(str(summ))
            ptr1 -= 1
            ptr2 -= 1

        # for eg. 99+1 = 100. Here carry is generated at the last position after the while loop. Hence check for carry again here

        if carry:
            result.append(str(carry))
        return "".join(result[::-1])

obj = Solution()
result1 = obj.addStrings("99","1")
result2 = obj.addStrings("101", "2")
print(result1)
print(result2)