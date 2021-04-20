from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != "-":
            # append + sign for coding purposes since positive number
            expression = "+" + expression

        numerator = []
        denominator = []

        i = 0
        while i < len(expression):
            # negative flag
            negative = True if expression[i] == "-" else False

            i += 1  # turn to the first digit
            n = 0  # for converting str to int char by char

            while expression[i].isdigit():
                n = (n * 10) + int(expression[i])  # to get the actual number e.g 12
                i += 1  # on "/"

            numerator.append(n if negative == False else -n)
            i += 1  # skip "/"  on 2
            d = 0
            while i < len(expression) and expression[i].isdigit():
                d = (d * 10) + int(expression[i])  # to get the actual number
                i += 1  # on +
            denominator.append(d)

        print(numerator, denominator)

        denom = 1
        for i in denominator:
            denom = denom * i

        for j in range(len(numerator)):
            numerator[j] = numerator[j] * denom // denominator[j]
        numo = sum(numerator)

        g = gcd(numo, denom)
        numo = numo // g
        denom = denom // g

        return str(numo) + "/" + str(denom)

obj = Solution()
print(obj.fractionAddition("-4/2+1/3"))