#https://www.acmicpc.net/problem/1726
'''
좌표따로 방향따로 정해주는 걸로 하면 되지않을까
방향까지 거리를 재야하는데 그러면 dfs를 해야할까 그러면 시간초과가일어나지않을까..
문제 발생 북쪽이면 동서는 1번만 움직이면되는데 시계방향으로 움직여서 에러가 생긴다.

쭉가는것을 1로 친다 그러면 중간에 멈추는것을 어떻게 판단하고 멈춰야할까...
'''


'''
북 동서 1 남 2
'''
def direct(a,b):
    if a in [0,1] and b in [0,1] and a!=b:
        return 2
    elif a in [2,3] and b in [2,3] and a!=b:
        return 2
    elif a == b:
        return 0
    else:
        return 1
# 2차원배열
# 
# 방향
def dfs(x,y,dir,dist):
    S = list()
    S.append((x,y,dir))
    count = dist
    while S:
        print(S)
        sx, sy, sdir = S.pop(0)
        count = visited[sx][sy]
        count += 1
        for d in range(4):
            d_count = count
            ndir = sdir
            d_count += direct(d,ndir) 
            nx = sx
            ny = sy  
            while 0<= nx < scale_x and 0<= ny < scale_y and li[nx][ny]== 0 and visited[nx][ny] == 0:
                visited[nx][ny] = d_count
                nx += dc[d]
                ny += dr[d] 
            if nx==end_x-1 and ny == end_y-1:
                visited[nx][ny]= d_count - 2 + direct(end_dir-1,ndir)
                return visited[nx][ny]
            else:
                visited[nx][ny] = d_count
                S.append((nx,ny,ndir))
        print(count)
        print(visited)
    return


scale_x, scale_y = map(int, input().split())
li= list()
for i in range(scale_x):
    li.append(list(map(int, input().split())))
start_x, start_y, start_dir = map(int, input().split())
end_x, end_y, end_dir = map(int, input().split())
visited = [[0 for _ in range(scale_y)] for _ in range(scale_x)]
# 1동 2서 3남 4북

dr = [1,-1,0,0]
dc = [0,0,-1,1]

print(dfs(start_x-1,start_y-1,start_dir,1),'ans')


#############################
from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, dir):
    q.append([x, y, dir])
    c[x][y][dir] = 1
    while q:
        x, y, dir = q.popleft()
        if x == x1-1 and y == y1-1 and dir == dir1-1: #도착했을때
            print(c[x][y][dir]-1)
            return
        turn_r(x, y, dir) # 오른쪽 돌고
        turn_l(x, y, dir) # 왼쪽 돌고
        nx = x + dx[dir]
        ny = y + dy[dir] # 이동
        if 0 <= nx < m and 0 <= ny < n: # 범위안이면
            if a[nx][ny] == 0:
                move(x, y, dir) #3칸 움직이면서 q에 삽입
        # else:
        #     turn_l(x, y, dir) #못움직이면 회전
        #     turn_r(x, y, dir)
        # 왜있음 이거?

'''

(1,1,동)
->
    (1,1,북) -> 3칸 확인
        -> (1,1,서) -> 3칸 확인
    (1,1,남) -> 3칸 확인



최대 3거리를 이동할수있는데
결과가나온다.
'''

def move(x, y, dir):
    cnt = 1
    nx = x; ny = y
    while cnt <= 3: # 세칸 이동
        nx += dx[dir]
        ny += dy[dir]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or a[nx][ny] == 1:
            return
        if c[nx][ny][dir] == 0:
            c[nx][ny][dir] = c[x][y][dir] + 1
            q.append([nx, ny, dir])
        cnt += 1


def turn_r(x, y, dir):
    if dir == 0: ndir = 2
    elif dir == 1: ndir = 3
    elif dir == 2: ndir = 1
    else: ndir = 0
    if c[x][y][ndir] == 0:
        c[x][y][ndir] = c[x][y][dir] + 1
        q.append([x, y, ndir])

def turn_l(x, y, dir):
    if dir == 0: ndir = 3
    elif dir == 1: ndir = 2
    elif dir == 2: ndir = 0
    else: ndir = 1
    if c[x][y][ndir] == 0:
        c[x][y][ndir] = c[x][y][dir] + 1
        q.append([x, y, ndir])

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
x0, y0, dir0 = map(int, input().split())
x1, y1, dir1 = map(int, input().split())

c = [[[0]*4 for _ in range(n)] for _ in range(m)]
q = deque()

bfs(x0-1, y0-1, dir0-1)