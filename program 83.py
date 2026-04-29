def score_of_parentheses(s):
    stack =
    
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
            
    return stack.pop()

s1 = "()()"
print(score_of_parentheses(s1))

s2 = "(()(()))"
print(score_of_parentheses(s2))

s3 = "((()))"
print(score_of_parentheses(s3))
