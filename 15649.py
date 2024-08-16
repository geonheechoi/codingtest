# N과 M (1)

n, m = map(int, input().split())
s = [] 
visited = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        # print(s)
        # print(visited)
        visited[i] = False
        
dfs()
