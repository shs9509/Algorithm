#https://www.acmicpc.net/problem/22944


# N, H, D = map(int,input().split())
# print(N,H,D)

# li = list()
# for i in range(N):
#     li.append(input())

# print(li)

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]



# for x in range(N):
#     for y in range(N):
#         if li[x][y] == 'S':
#             start_x = x
#             start_y = y
#         elif li[x][y]== 'E':
#             end_x = x
#             end_y = y

# answer = list()

# def dfs():
#     V = [[0 for _ in range(N)] for _ in range(N)]
#     V[start_x,start_y] = H
#     tmp = [(start_x,start_y,H,0,0)]
#     while(tmp):
#         x,y,h,d,distance = tmp.pop(0)
#         for j in range(4):
#             X = x+dx[j]
#             Y = y+dy[j]
#             if 0<=X<N and 0<=Y<N:
#                 if li[X][Y] =='E':
#                     print(distance+1)
#                     break
#                 elif li[X][Y] =='U':
#                     if d == 0:
#                         tmp.append((X,Y,h-1,D,distance+1))
#                     else:
#                         tmp.append((X,Y,h,D,distance+1))
#                 else:
#                     V[X][Y] = V[x][y]+1
#                     tmp.append((X,Y,h-1))
# dfs()

from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,h,d = map(int, input().split())
board = []

sx=sy=-1
for x in range(n):
    board.append(list(input().strip()))
    if sx==-1:
        for y in range(n):
            if board[x][y] == 'S':
                sx,sy = x,y

def solv():
    visited = [[0]*n for _ in range(n)]
    q = deque([(sx,sy,h,0,0)])
    visited[sx][sy] = h

    while q:
        x,y,now_h,now_d,cnt = q.pop()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx,ny):
                if board[nx][ny] == 'E':
                    print(cnt+1)
                    return
                nxt_h = now_h # 현재피
                nxt_d = now_d # 현재 우산 내구도

                if board[nx][ny] == 'U':
                    nxt_d = d

                if nxt_d == 0:
                    nxt_h -= 1
                else:
                    nxt_d -= 1

                if nxt_h == 0:
                    continue

                if visited[nx][ny] < nxt_h:
                    visited[nx][ny] = nxt_h
                    q.appendleft((nx,ny,nxt_h,nxt_d,cnt+1))

    print(-1)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()