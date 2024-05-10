import sys
sys.setrecursionlimit(10**7)

def solution(s):
    stack = []
    
    for letter in s:
        if not stack:
            stack.append(letter)
        else:
            if stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

    return 1 if not stack else 0
    
def recursive_solution(s):
    if len(s) == 0:
        return 1
    
    elif len(s) == 1:
        return 0
    
    elif len(s) == 2:
        return 1 if s[0] == s[1] else 0
    
    else:
        for i in range(len(s)):
            if i < len(s) - 2:
                if s[i] == s[i+1]:
                    return solution(s[:i] + s[i+2:])
            elif i == len(s) - 2:
                if s[i] == s[i+1]:
                    return solution(s[:i])
            elif i == len(s) - 1:
                return 0
            
