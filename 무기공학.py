# #https://www.acmicpc.net/problem/18430
# ## 어려운거같은디..
# r,c = list(map(int,input().split()))
# li = list()
# for i in range(c):
#     li.append(list(map(int,input().split())))

# visit = [ [True for _ in range(c)] for _ in range(r) ]

# one =[[1,0],[1,0],[-1,0],[-1,0]]
# two =[[0,1],[0,-1],[0,-1],[0,1]]

# result =[0]

# def dfs(x,y,v,value):
#     result.append(value)
#     for i in range(4):
#         X1 = x+one[i][0]
#         Y1 = y+one[i][1]
#         X2 = x+two[i][0]
#         Y2 = y+two[i][1]
#         if v[x][y] and 0<=X1<r and  0<=X2<r and 0<=Y1<c and 0<=Y2<c and v[X1][Y1] and v[X2][Y2]:
#             v[X1][Y1] = False
#             v[X2][Y2] = False
#             v[x][y] = False
#             if y==c:
#                 if x==r:
#                     result.append(value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
#                     return
#                 else:
#                     dfs(x+1,0,v,value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
#             else:
#                 dfs(x,y+1,v,value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
#         else:
#             if y==c-1:
#                 if x==r-1:
#                     result.append(value)
#                     return
#                 else:
#                     dfs(x+1,0,v,value)
#             else:
#                 dfs(x,y+1,v,value)
            

# dfs(0,0,visit,0)
# print(result) 

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
used = [[0 for _ in range(M)] for _ in range(N)]
dy = [[0, 1], [0, -1], [-1, 0], [0, 1]]
dx = [[-1, 0], [-1, 0], [0, 1], [1, 0]]
answer = 0


def traverse(power, cy, cx):
    global answer

    for y in range(cy, N):
        for x in range(cx if y == cy else 0, M):
            if used[y][x] == 1:
                continue
            for i in range(4):
                flag = True
                for j in range(2):
                    ny, nx = y + dy[i][j], x + dx[i][j]

                    if 0 > ny or ny >= N or nx < 0 or nx >= M or used[ny][nx] == 1:
                        flag = False
                        break
                if flag is True:
                    total = 0
                    used[y][x] = 1
                    for j in range(2):
                        ny, nx = y + dy[i][j], x + dx[i][j]
                        used[ny][nx] = 1
                        total += board[ny][nx]
                    traverse(power + total + board[y][x] * 2, y if x + 1 < M else y + 1, x + 1 if x + 1 < M else 0)
                    for j in range(2):
                        ny, nx = y + dy[i][j], x + dx[i][j]
                        used[ny][nx] = 0
                    used[y][x] = 0
    answer = max(answer, power)

traverse(0, 0, 0)
print(answer)