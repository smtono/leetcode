def isValid(s: str) -> bool:
    valid = False
    stack = []
    
    for character in s:
        if character in ["(", "[", "{"]:
            stack.append(character)
        else:
            match = stack.pop()
            if character is ')':
                if match is not '(':
                    return False
            if character is ']':
                if match is not '[':
                    return False
            if character is '}':
                if match is not '{':
                     return False
    if not stack:
        valid = True
    
    return valid

print(isValid("{)"))