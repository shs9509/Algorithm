#https://www.acmicpc.net/problem/1600

jump = int(input())
size_y, size_x = map(int,input().split())
result =list()
V = list()
for i in range(size_x):
    V.append(list(map(int,input().split())))

dr = [0,0,1,-1]
dc = [1,-1,0,0] # 원숭이
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1] # 말

def bfs():
    lis = [(0,0,jump)]
    visit = [[[0 for _ in range(99)] for _ in range(size_y)] for _ in range(size_x)]
    while lis:
        x, y, remain_jump = lis.pop(0)
        if x == (size_x - 1) and y == (size_y - 1):
            result.append(visit[x][y][remain_jump])
            return
        # 점프가 있으면 점프를 한경우
        if remain_jump:
            for i in range(8):
                X = x+dx[i]
                Y = y+dy[i]
                if 0 <= X < size_x and 0 <= Y < size_y and V[X][Y] == 0 and visit[X][Y][remain_jump-1] == 0:
                    visit[X][Y][remain_jump-1] = visit[x][y][remain_jump] + 1
                    lis.append((X,Y,remain_jump-1))
        # 점프를 안했을 경우
        for j in range(4):
            XX = x + dr[j]
            YY = y + dc[j]
            if 0 <= XX < size_x and 0 <= YY < size_y and V[XX][YY] == 0 and visit[XX][YY][remain_jump] == 0:
                visit[XX][YY][remain_jump] = visit[x][y][remain_jump] + 1
                lis.append((XX, YY,remain_jump))

bfs()
if result == []:
    print(-1)
else:
    print(min(result))



걸 점 걸 걸 걸 도착 (점 1)

걸 걸 걸 점 걸 도착 (점 0)

