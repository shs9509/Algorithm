#https://www.acmicpc.net/problem/7579

from collections import deque

col, row , height = list(map(int, input().split())) #가로 세로 높이
section = [[list(map(int, input().split())) for ro in range(row)] for he in range(height)]    # 토마토 판

dr = [1,0,0,-1,0,0]
dc = [0,1,-1,0,0,0]
dh = [0,0,0,0,1,-1] # 6가지의 방향
max_day = 0 # 최종날짜를 나타내는값
S = deque()
for h in range(height):
    for y in range(row):
        for x in range(col):
            if section[h][y][x] == 1:   # 토마토가 안익으면 큐에넣는다.
                S.append((h,y,x,0))   ## 튜플로하면 더좋다 ##
while len(S) != 0:              # BFS
    start_h, start_y, start_x, start_day = S.popleft()
    if max_day <= start_day:    # 날짜가 더 큰경우를 넣는다.
        max_day = start_day
    for i in range(6):
        H = start_h + dh[i]
        Y = start_y + dr[i]
        X = start_x + dc[i]
        L = start_day + 1
        if 0 <= H < height and 0 <= Y < row and 0 <= X < col and section[H][Y][X] == 0:
            section[H][Y][X] = 1   # 거치는 토마토를 전부 1로 체크
            S.append((H,Y,X,L))

flag = False
if max_day == 0:
    print(0)
else:
    for He in range(height):    # BFS를 거치고 토마토 판에 0 있으면 -1 출력
        for R in range(row):
            if 0 in section[He][R]:
                print(-1)
                flag = True
                break
        if flag:
            break
    else:   # 0일 없으면 걸렸던 날짜를 출력
        print(max_day)
