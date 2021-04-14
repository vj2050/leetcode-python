def minRemoveToMakeValid(s):
    string_list = list(s)
    stack = []

    for i, char in enumerate(string_list):

        if char == "(":
            stack.append(i)  # keep pushing the index of ( in stack. Equal number of of push and pops shud happen
        elif char == ")":
            if stack:  # if stack is still not empty after equal number of pops, hence extra parantheses
                stack.pop()
            else:
                # stack empty,hence this indexed element is the odd one out and use its index and delete it from string i.e more ) than (
                string_list[i] = ""

    # now have all locations of remaining unpopped parantheses: more ( than )
    for i in stack:
        string_list[i] = ""

    return "".join(string_list)

print(minRemoveToMakeValid("lee(t(c)o)de)"))