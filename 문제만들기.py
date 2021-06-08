from collections import deque
def corona():
    #코로나 확산
    next_virus = []
    while virus:
        pr,pc = virus.popleft()
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
                next_virus.append((nr,nc))
    for p in next_virus:
        i,j = p[0],p[1]
        arr[i][j] = -1
def vaccination():
    #백신접종
    next_safe = []
    while vaccine:
        pr,pc = vaccine.popleft()
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] != 1:
                next_safe.append((nr,nc))
    for p in next_safe:
        i,j = p[0],p[1]
        arr[i][j] = 1
N, M = map(int,input().split())
virus = deque()
vaccine = deque()
arr = []
for r in range(N):
    tmp = list(map(int,input().split()))
    for c in range(M):
        if tmp[c] == -1:
            virus.append((r,c))
        elif tmp[c] == 1:
            vaccine.append((r,c))
    arr.append(tmp)
dr = [-1,1,0,0]
dc = [0,0,-1,1]
day = 1
if len(virus)==0:
    print(0)
elif len(vaccine)==0 and len(virus)!=0:
    print('fail')
else:
    while True:
        corona()
        vaccination()
        for r in range(N):
            for c in range(M):
                if arr[r][c] == -1:
                    virus.append((r,c))
                elif arr[r][c] == 1:
                    vaccine.append((r,c))
        if len(virus) == 0:
            break
        else:
            day += 1
    print(day)