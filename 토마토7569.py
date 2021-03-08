def cons(li, row, col, char):  # li = 색깔배치, scale = 배치 크기, char = 해당하는 색깔
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]
    count = 0   # 구역 숫자
    visited = [['o' for j in range(row)] for k in range(col)] # 확인한 색깔 체크용리스트
    for x in range(col):
        for y in range(row):
            if (li[x][y] in char) and (visited[x][y] != 'V'):   # 원하는색깔이며 방문하지 않았다!
                start_x = x
                start_y = y # x,y 그대로쓰면 밑에서 위의 for문의 xy가 바뀜
                count += 1  # 구역 추가 
                S = list()
                S.append([start_x,start_y])
                while len(S) != 0:
                    start_x, start_y = S.pop()
                    visited[start_x][start_y] = 'V' # 방문 체크해주기
                    for i in range(4):
                        X = start_x + dr[i]
                        Y = start_y + dc[i]
                        if 0 <= X < col and 0 <= Y < row:
                            if li[X][Y] in char and visited[X][Y] != 'V':
                                S.append([X,Y])
    return count

row1, col1, height = list(map(int, input().split()))
section = list()
for i in range(row1):
    section.append(list(map(int ,input().split())))
if cons(section, row1, col1, [0,1]) != 1:
    print(-1)
