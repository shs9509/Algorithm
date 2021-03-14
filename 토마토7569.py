#https://www.acmicpc.net/problem/7579

from collections import deque

row, col = list(map(int, input().split())) #가로 세로
section = list()    # 토마토 판
go = 1 
for co in range(col):
    section.append(list(map(int ,input().split())))

for search1 in section: # 다익은경우 판별
    if 0 in search1:
        break
else:
    go = 0 

if go: # 다 안익었으면 시작
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]
    max_day = 0 # 최종날짜를 나타내는값
    S = deque()
    for x in range(col):
        for y in range(row):
            if section[x][y] == 1:   # 토마토가 안익으면 큐에넣는다.
                S.append((x,y,0))   ## 튜플로하면 더좋다 ##
    while len(S) != 0:              # BFS
        start_x, start_y, start_day = S.popleft()
        if max_day <= start_day:    # 날짜가 더 큰경우를 넣는다.
            max_day = start_day
        for i in range(4):
            X = start_x + dr[i]
            Y = start_y + dc[i]
            L = start_day + 1
            if 0 <= X < col and 0 <= Y < row and section[X][Y] == 0:
                section[X][Y] = 1   # 거치는 토마토를 전부 1로 체크
                S.append((X,Y,L))

    for search in section:  # BFS를 거치고 토마토 판에 0 있으면 -1 출력
        if 0 in search:
            print(-1)
            break
    else:   # 0일 없으면 걸렸던 날짜를 출력
        print(max_day)
else:   # 애초에 다 익었다면 0 출력
    print(go)