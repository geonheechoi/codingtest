# 시간 초과
# from collections import deque 

N, K = map(int, input().split())

circle = list(range(1, N+1))

print("<", end="")
while circle:
    if len(circle) >= K:
        print(circle[K-1], end=", ")
        circle = circle[:K-1] + circle[K:]
        for _ in range(K-1):
            circle = circle[1:] + [circle[0]]
    else:
        k = (K - len(circle)) % len(circle)
        print(circle[k-1], end=", " if len(circle) > 1 else "")
        if len(circle) == 1:
            break
        circle = circle[:k-1] + circle[k:]  
    
print(">")
