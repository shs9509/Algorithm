#https://www.acmicpc.net/problem/1941

arr = [input() for i in range(5)] #입력

prin = [[0 for i in range(5)] for j in range(5)]

diry = [1,-1,0,0]
dirx = [0,0,1,-1]

visit = [[0 for i in range(5)] for j in range(5)] # 방문표시
ans = 0
p = []

def check(s):
    global visit
    y = s//5
    x = s%5
    
    for i in range(4):
        ty = y+diry[i]
        tx = x+dirx[i]
        
        if ty>=0 and ty<5 and tx>=0 and tx<5:
            if visit[ty][tx]==0:
                if (ty*5+tx) in p:
                    visit[ty][tx] = 1#방문표시를 1로한다.
                    check((ty*5+tx)) #다음꺼.
    
    
            
def dfs(cnt,idx,yn):
    global ans #정답 횟수
    global visit
    
    if yn>=4 or 25-idx<7-cnt: #임도연이 4명이상, 남은 인덱스를 다채워도 7명이 안될떄.
        return
        
    if cnt==7: # 7번을 진행했을떄     
        check(p[0])#p에 쌓아온 인덱스로 체크(서로 연결되었는지)
        if sum(sum(visit,[]))==7: #1로 방문표시했거가 7개면 7공주!
            ans+=1  # 하나의 방법인걸로 추가
        visit = [[0 for i in range(5)] for j in range(5)] # 방문표시 리셋
        return
    
    y = idx//5
    x = idx%5
    
    '''
    (Y) 1 1 1
     1 1 1 1 1
    11111
    '''
    p.append(idx) # p 에 해당위치를 쌓는다.
    if arr[y][x]=='Y': # 임도연이면 임도연수 추가한상태로 dfs 돌림
        dfs(cnt+1,idx+1,yn+1) # 체크한사람수, 위치, 임도연수
    else:
        dfs(cnt+1,idx+1,yn) #cnt 임소연으로 다음진행
    
    p.pop()
    dfs(cnt,idx+1,yn) # 순회
    
dfs(0,0,0)
print(ans)

# 세가지 경우, 임도연으로 시작할지, 임소연으로 시작할지, 다음부터 시작할지

###

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
princess = deque()
ans = set()
A = [[] for _ in range(5)]
visit = [[False] * 5 for _ in range(5)]

def go(n, cnt):
    if (cnt + (7 - n) < 4): #cnt가 임도연
        return

    if n == 7:
        if cnt >= 4:
            temp = list(princess)
            temp.sort()
            temp = tuple(temp)
            ans.add(temp)
        return

    possible = set()
    for node in princess:
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx == 5 or ny == 5 or visit[nx][ny]:
                continue

            possible.add((nx,ny))

    for node in possible:

        visit[node[0]][node[1]] = True
        princess.append(node)
        if A[node[0]][node[1]] == 'S':
            go(n+1, cnt+1)
        else:
            go(n+1, cnt)
        princess.pop();
        visit[node[0]][node[1]] = False

for i in range(5):
    A[i] = list(input().rstrip())

for i in range(5):
    for j in range(5):
        if A[i][j] == 'S':
            visit[i][j] = True
            princess.append((i,j))
            go(1,1)
            princess.popleft()

print(len(ans))