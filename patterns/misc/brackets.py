def brackets(string):
    stack = []
    brackets = {
        '{':'}',
        '[':']',
        '(':')'
    }
    # iterate string
    for i in range(len(string)):
        # if opening bracket, add to stack
        if string[i] in brackets:
            stack.append(string[i])
        # if closing bracket, pop and check
        elif len(stack) > 0: 
            bracket = stack.pop(len(stack)-1)
            # if not matching, return 0
            if string[i] != brackets[bracket]:
                return False
        else:
            return False
        

    # if remaining brackets in stack, return 0
    if len(stack) > 0:
        return False
    return True

print(brackets('{[()()]}')) # true
print(brackets('{[}])}')) # false
print(brackets(')(')) # false
print(brackets('[)()]')) # false
print(brackets('{{{{')) # false
print(brackets('((()))(()')) # false