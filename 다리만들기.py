#https://www.acmicpc.net/problem/2146
'''
가장 멀리떨어져있는것을 찾아야하는데
그걸 어케 찾냐고
한영역을 기준으로 bfs를 돌린다?
영역의 좌표를 리스트에 넣고 그걸로 bfs 돌리면 되지 않을까
+
3개의 다리를 모두 구해봐야한다.

'''
import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

scale = int(input())
land = list()
for i in range(scale):
    land.append(list(map(int,input().split())))

check = [[False] * scale for _ in range(scale)] # 섬 확인시 체크용리스트
ans = sys.maxsize # 이러면 최대값이 늘어난다.
count = 1


### dfs ###
def dfs(x,y): # dfs를 통해서 섬들을 체크해준다. 1번섬, 2번섬, 3번섬
    global count
    S =list()
    S.append((x,y))
    while S:
        x,y =S.pop()
        check[x][y] = True
        land[x][y] = count
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if nx < 0 or nx >= scale or ny < 0 or ny >= scale:
                continue
            if check[nx][ny] == False and land[nx][ny]:
                S.append((nx, ny))

### 섬체크 ###
for x in range(scale):
    for y in range(scale):
        if check[x][y] == False and land[x][y] == 1:
            dfs(x, y)
            count += 1


### bfs ###
def bfs(z):
    global ans
    dist = [[-1] * scale for _ in range(scale)] # 거리를 나타내는 배열
    q = deque()

    for x in range(scale):
        for y in range(scale):
            if land[x][y] == z:
                q.append((x, y)) # q에 해당섬의 좌표를 다넣는다.
                dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dc[i], y + dr[i]
            if nx < 0 or nx >= scale or ny < 0 or ny >= scale: # 범위를 넘어가면
                continue
            if land[nx][ny] > 0 and land[nx][ny] != z:  # 다른섬에 도착했을때
                ans = min(ans, dist[x][y])
                return
            if land[nx][ny] == 0 and dist[nx][ny] == -1: # 방문 안한곳
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


for i in range(1, count): # 1번섬부터 쭉 돌려본다.
    bfs(i)

print(ans)



# sys.setrecursionlimit(10 ** 6)

# ### dfs ###
# def dfs(x,y): # dfs를 통해서 섬들을 체크해준다. 1번섬, 2번섬, 3번섬
#     global count
#     check[x][y] = True
#     land[x][y] = count
    
#     for i in range(4):
#         nx, ny = x + dr[i], y + dc[i]
#         if nx < 0 or nx >= scale or ny < 0 or ny >= scale:
#             continue
#         if check[nx][ny] == False and land[nx][ny]:
#             dfs(nx,ny)

# ### 섬체크 ###
# for x in range(scale):
#     for y in range(scale):
#         if check[x][y] == False and land[x][y] == 1:
#             dfs(x, y)
#             count += 1
#https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2146-%EB%8B%A4%EB%A6%AC%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC