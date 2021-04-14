'''

Given a binary string  of length , you can cyclically shift this string any number of times. For example, consecutively applying cyclic shift operation to the binary string "" you will get "", "" and so on.

Let  be the decimal representation of string . Find the greatest power of  with which  can be divisible with, if it can be divisible with arbitrarily large power print "".

For the result, you are required to print a single integer denoting the maximum power of  by which  can be divisible with.

For example if string "", we can cyclically shift  time to get string "" which in decimal is  and is divisible with , hence the answer is .

Input Format

The first and only line of input contains string .

Constraints

Output Format

Print a single integer denoting the maximum power of  by which  can be divisible with.

Sample Input 0

0011
Sample Output 0

2
Explanation 0

We can cyclically shift the string  times to get "" which is divisible by  hence the answer is .

Sample Input 1

111
Sample Output 1

0
Explanation 1

The string will remain same even after any number of cyclic shifts, and the given string in decimal is , which is divisible by  hence the answer is .

'''

s = "0011"
s = list(s)
shift = len(s)
result = 0
li = []
for i in range(0, shift):
    temp = s[0]
    for j in range(len(s) - 1):
        s[j] = s[j + 1]

    s[len(s) - 1] = temp
    string2 = "".join(s)
    print(string2)

    intstr = int(string2, 2)
    print(intstr)
    if intstr % 2 == 0:
        li.append(intstr)
print(li)

num = max(li)
cnt = 0
i = 1

for i in range(1, 100):
    if num % 2 ** i == 0:
        cnt += 1
        i += 1
    else:
        break

print(cnt)
