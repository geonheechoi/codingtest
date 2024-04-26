def solution(dirs):
    count = 0
    visited = []
    current = (0, 0)
    
    for dir in dirs:
        x, y = current

        if dir == "U":
            if y < 5:
                y += 1
        elif dir == "D":
            if y > -5:
                y -= 1
        elif dir == "L":
            if x > -5:
                x -= 1
        elif dir == "R":
            if x < 5:
                x += 1
        
        if current != (x,y):
            path = (current, (x,y))
            if (current, (x,y)) in visited or ((x,y), current) in visited:
                pass
            else:
                count += 1
            current = (x,y)
            visited.append(path)
            
    return count
