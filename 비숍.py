#https://www.acmicpc.net/problem/1799

def check(idx):
    c = idx%2 #홀수패턴인지 짝수패턴인지 판별
    i, j = idx//n, idx%n
    
    for d in range(4):
        x, y = i+dx[d], j+dy[d] 
        while 0<=x<n and 0<=y<n: 
            if visited[x*n + y]: # 방문한적있으면 취소
                return False 
            x += dx[d] 
            y += dy[d]  # 대각선 끝까지 탐색
    return True 


def dfs(idx, c, cnt): #좌표, 짝홀패턴, 개수
    if n*n-idx+1+cnt <= ans[c] or idx >= n*n: # 순회돈 나머지가 ans값보다 작거나, idx가 범위넘어가면
        return 
    ans[c] = max(ans[c], cnt) 

    x, y = idx//n, idx%n  # x,y좌표
    j = y 
    for i in range(x, n):
        while j < n: 
            v = i*n + j # 1차원배열일때의 좌표
            if not visited[v] and chess[i][j] == 1 and check(v): 
                # 방문안하고, 1인공간, 범위가 안넘어감
                visited[v] = True 
                dfs(v, c, cnt+1) # 방문체크하고 개수늘림()
                visited[v] = False 
            j += 2 
            #짝수칸씩 이동해야됨
        j = (c+1)%2 if i%2 == 0 else c #세로줄마다 j의 시작점이 달라야함

'''
n = 3

흑 백 흑

백 흑 백

흑 백 흑

-> [흑, 백, 흑, 백, 흑, 백, 흑, 백, 흑]

 
n = 2

흑 백

백 흑

-> [흑, 백, 백, 흑]

'''

n = int(input()) 
chess = [list(map(int, input().split())) for _ in range(n)] 
dx = [1, -1, 1, -1]
dy = [1, 1, -1, -1] 
visited = [False] * (n**2) 
print(visited)
ans = [0, 0] 
 # 짝수는 0, 홀수는 1 체스판에서 비숍이 움직일수있는 제한은 2가지 
dfs(0, 0, 0) 
dfs(1, 1, 0) 
print(sum(ans))