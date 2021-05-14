class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return str(0)
        fraction = ""
        if bool(numerator < 0) ^ bool(denominator < 0):
            fraction = fraction + "-"

        fraction = fraction + str(abs(numerator) // abs(denominator))
        remainder = abs(numerator) % abs(denominator)

        if remainder == 0:
            return fraction
        else:
            fraction += "."

        print("part1 : ", fraction)
        print("remainder ", remainder)
        dictt = {}
        while (remainder != 0):
            if remainder in dictt:
                fraction = fraction[:dictt[remainder]] + "(" + fraction[dictt[remainder]:] + ")"
                break;

                # pattern repeated
            else:
                dictt[remainder] = len(fraction)
                remainder = remainder * 10
                print("fraction for part 2", fraction)
                fraction = fraction + str(remainder // abs(denominator))
                remainder = remainder % abs(denominator)
        return fraction
        # print("fraction", fraction)
obj = Solution()
print(obj.fractionToDecimal(-2,7))