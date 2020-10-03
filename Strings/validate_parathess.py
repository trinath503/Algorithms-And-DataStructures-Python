
def validate_parathesis(given_array):
    stack , lookup = [], {"(": ")", "{": "}", "[": "]"}
    for each_param in given_array:
        # print(stack,each_param)
        if each_param in lookup:
            stack.append(each_param)
        elif len(stack) ==0 or lookup[stack.pop()] != each_param:
            return False
    return len(stack) ==0

# Time:  O(n)
# Space: O(n)
print(validate_parathesis("()[]{}"))
print(validate_parathesis("([)]"))