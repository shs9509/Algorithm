#L을 찾아서 좌표를 리스트에 넣고
# 그 L을 일일이 pop 하면서 거리를 찾는다?
# L 찾을 때마다 bfs 돌려서 최대값 비교?

from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q.append((x, y))
    visit = [[0]*col for _ in range(row)]
    visit[x][y] = 1
    num = 0
    while q:
        x, y = q.popleft()
        # num += 1
        # for _ in range(len(S)):
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < row and 0 <= Y < col:
                if island[X][Y] == 'L' and visit[X][Y] == 0:
                    visit[X][Y] = visit[x][y] + 1 
                    num = max(num, visit[X][Y])
                    q.append((X, Y))
    return num-1

row, col = map(int, input().split())
island = [list(map(str, input())) for _ in range(row)]
q = deque()

cnt = 0
for i in range(row):
    for j in range(col):
        if island[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))
print(cnt)