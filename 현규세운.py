def solution(s):
    stack=[]
    
    for i in range(len(s)):
        if stack:
            if s[i] is stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    return   0 if stack else 1
