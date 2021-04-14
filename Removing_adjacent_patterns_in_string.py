# SHIVANI ASSESSMENT EASY :

s = "CBACD"

stack = []

for each in s:
    # print(each)
    if stack and (stack[-1] + each in ["AB", "BA", "CD", "DC"]):
        stack.pop()     #
        #print("stack ", stack, each)
    else:
        stack.append(each)
print(stack)
print("".join(stack))