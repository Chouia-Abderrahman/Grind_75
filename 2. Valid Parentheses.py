def isValid(s : str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    # this is considered a hashmap and the first characters are
    close_to_open = {")":"(","]":"[","}":"{"}

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))




