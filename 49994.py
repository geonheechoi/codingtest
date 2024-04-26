def solution(dirs):
    count = 0 # 처음 걸어본 길의 개수 카운트
    visited = [] # 방문한 길 리스트
    current = (0, 0) # 현재 위치 - 원점이 (0, 0)
    
    for dir in dirs:
        x, y = current

        if dir == "U":
            if y < 5: # 벽에 부딪히면 움직임 무시
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
        
        if current != (x,y): # 위치가 바뀌었으면
            path = (current, (x,y)) # 방금 지나온 길
            if (current, (x,y)) in visited or ((x,y), current) in visited: # 방금 지나온 길이 이미 방문한 길이면 & ((p1,q1), (p2,q2)) ~ ((p2,q2), (p1,q1))
                pass
            else: # 방금 지나온 길이 방문한 길이 아니면
                count += 1 # 카운트 증가
            current = (x,y) # 위치 업데이트
            visited.append(path) # 방문한 길 업데이트
            
    return count
