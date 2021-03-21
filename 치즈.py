'''
0일때 사방탐색 하면되는거 아닌가? 안되네..

네방향에서 체크? 안되네..

뭔가 0인걸로 dfs 조지면 되지않을까... 그러면 안에있는 빈공간도 처리가된다.

0인걸 찾아서 c로 만들고 c개수 체크, c인걸 한꺼번에 0으로 처리하면서 +1


'''
cheese_pan = list()
row, col = list(map(int, input().split()))
for r in range(row):
    cheese_pan.append(list(map(int, input().split())))

dr = [0,0,1,-1]
dc = [-1,1,0,0]
count = 0
S = list()

# 처음 세팅
setting = 1

while setting:
    S.append((0,0))
    setting = 0
    count_cheese = 0
    visit = [[1] * col for _ in range(row)] #방문 안한상태 '1'
    count += 1
    visit[0][0] = 0  
    while S:
        x,y = S.pop() 
        for i in range(4):
            X = x+dr[i]
            Y = y+dc[i]
            if 0<= X < row and 0<= Y < col and cheese_pan[X][Y]==1 and visit[X][Y]:
                cheese_pan[X][Y] = 0
                visit[X][Y] = 0
                count_cheese += 1
            elif 0<= X < row and 0<= Y < col and cheese_pan[X][Y]==0 and visit[X][Y]:
                visit[X][Y] = 0 # 방문했음
                S.append((X,Y))
    for r in cheese_pan:
        if 1 in r:
            setting = 1
print(count)
print(count_cheese)

