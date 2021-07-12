#0708 넴모넴모 (Easy) : https://www.acmicpc.net/problem/14712

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 1-index
Map = [ [ 0 for _ in range(M + 1) ] for __ in range(N + 1) ]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return
    
    y = cnt // M + 1
    x = cnt  % M + 1
    
    dfs(cnt + 1)
    if Map[y - 1][x] == 0 or Map[y][x - 1] == 0 or Map[y - 1][x - 1] == 0: # 만약 놓을 수 있는 곳이라면
        Map[y][x] = 1
        dfs(cnt + 1)
        Map[y][x] = 0
dfs(0)
print(answer)

##################################

# a, b = map(int, input().split())

# visit = [[1 for _ in range(b)] for _ in range(a)]
# count = 0

# dr = [1,1,0]
# dc = [1,0,1]

# def dfs(c):
#     global count
#     if c == a*b:
#         count +=1
#         return
#     for x in range(a):
#         for y in range(b):
#             if visit[x-1][y-1] or visit[x-1][y] or visit[x][y-1]:
#                 visit[x][y] = 1
#                 dfs(c+1)
#                 visit[x][y] = 0
# dfs(0)
# print(count)