# https://www.acmicpc.net/problem/17836
# 그람 구하고 최단거리 vs 그냥가기
# import copy
# row, col,time = list(map(int,input().split()))
# li = list()

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# for i in range(row):
#     li.append(list(map(int,input().split())))

# for x in range(row):
#     for y in range(col):
#         if li[x][y]==2:
#             sword = [x,y]

# visit = copy.deepcopy(li)
# result = list()
# min_val= 9999999999
# def dfs(x,y,V,count):
#     global min_val
#     if count > time or count > min_val:
#         return
#     if x == row-1 and y == col-1:
#         if min_val > count:
#             min_val = count
#             result.append(count)
#         return
#     else:
#         for i in range(4):
#             X = x+dx[i]
#             Y = y+dy[i]
#             if 0<=X<row and 0<=Y<col and V[X][Y]!="V":
#                 if li[X][Y]==0:
#                     V[X][Y] = "V"
#                     dfs(X,Y,V,count+1)
#                     V[X][Y] = 0
#                 elif li[X][Y] ==2:
#                     dfs(row-1,col-1,V,count+row-X-1+col-Y-1+1)
# visit[0][0]="V"
# dfs(0,0,visit,0)
# if len(result)==0:
#     print("Fail")
# else:
#     if min(result) > time:
#         print("Fail")
#     else:
#         print(min(result))

#####################################################################

import copy
from collections import deque
row, col,time = list(map(int,input().split()))
li = list()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(row):
    li.append(list(map(int,input().split())))

for x in range(row):
    for y in range(col):
        if li[x][y]==2:
            sword = [x,y]

visit = [[9999999 for _ in range(col)] for _ in range(row)]
visit[0][0] =0
result = list()
min_val= 9999999999
def dfs():
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft() # 주의

        if x==row-1 and y==col-1:
            return visit[row-1][col-1]
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0<=X<row and 0<=Y<col:
                if li[X][Y]==0 and visit[x][y] < visit[X][Y]:
                    visit[X][Y] = min(visit[X][Y],visit[x][y]+1)
                    q.append((X,Y))
                elif li[X][Y]==2:
                    visit[X][Y] = min(visit[X][Y],visit[x][y]+1)
                    visit[row-1][col-1] = min(visit[row-1][col-1], visit[X][Y]+row-1-X+col-1-Y)
        print(visit)
print(dfs())
if visit[row-1][col-1]>time:
    print("Fail")
else:
    print(visit[row-1][col-1])

##########################################################################

import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()
 
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
 
n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
tmp = 123456789
 
def bfs():
    global tmp
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
 
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 2:
            tmp = abs(n - 1 - x) + abs(m - 1 - y) + visited[x][y] - 1
        if x == n - 1 and y == m - 1:
            return min(visited[x][y] - 1, tmp)
 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
    return tmp
 
 
res = bfs()
print("Fail" if(res > t) else res)

#############################################################################

N, M, T = map(int,input().split())
li= list()
for i in range(N):
    li.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if li[i][j]==2:
            sword_x=i
            sword_y=j

dx =[1,-1,0,0]
dy =[0,0,-1,1]
# print(li)
now =0
tmp = [(0,0)]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0]=True
check=True
while(tmp):
    x,y = tmp.pop(0)
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<N and 0<=Y<M and visited[X][Y]==False:
            if X==N-1 and Y==M-1:
                li[X][Y] = li[x][y]+1
                visited[X][Y]=True
                tmp =[]
                break
            if li[X][Y]==1:
                continue
            elif li[X][Y]==0:
                tmp.append((X,Y))
                li[X][Y] = li[x][y]+1
                visited[X][Y]=True
            elif li[X][Y]==2:
                li[X][Y] = li[x][y]+(M-1-Y)+(N-1-X)+1
                visited[X][Y]=True
# print(visited)
# print(now)
# print(li)
if visited[sword_x][sword_y]==True:
    if visited[N-1][M-1]==True:
        if min(li[sword_x][sword_y],li[N-1][M-1])>T:
            print("Fail")
        else:
            print(min(li[sword_x][sword_y],li[N-1][M-1]))
    elif li[sword_x][sword_y] > T:
        print("Fail")
    else:
        print(li[sword_x][sword_y])
elif visited[N-1][M-1]==True:
    if li[N-1][M-1] > T:
        print("Fail")
    else:
        print(li[N-1][M-1])
else:
    print('Fail') 