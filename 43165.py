def solution(numbers, target):
    stack = [(0, 0)]
    result = 0
    
    while stack:
        current, level = stack.pop()
        directions = [
            (current + numbers[level], level + 1),
            (current - numbers[level], level + 1)
        ]
        
        for next_current, next_level in directions:
            if next_level == len(numbers):
                if next_current == target:
                    result += 1
                continue
            
            stack.append((next_current, next_level))
            
    return result
