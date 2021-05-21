def dfs(r,c):
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    S = list()
    S.append((r,c))
    count = 0
    while S:
        x,y = S.pop(0)
        count = visit[x][y]+1
        for i in range(4):
            dx = x+dr[i]
            dy = y+dc[i]
            if 0<=dx<row and 0<=dy<col and li[dx][dy]=='L' and visit[dx][dy]>count:
                visit[dx][dy] = count
                S.append((dx,dy))
    return

tc = int(input())
for tc_num in range(tc):
    row, col = map(int,input().split())
    li = list()
    W_li = list()
    visit = [[row*col for c in range(col)]for r in range(row)]
    for i in range(row):
        li.append(list(map(str,input())))
    for x in range(row):
        for y in range(col):
            if li[x][y]=='W':
                visit[x][y] = 0
                W_li.append((x,y))
    for W in W_li:
        X,Y = W
        dfs(X,Y)
    ans = 0
    print(visit)
    for v in visit:
        ans+=sum(v)
    print('#{} {}'.format(tc_num+1,ans))

###################################################################

from collections import deque

def dfs(lis):
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    S =deque()
    for n in lis:
        S.append(n)
    count = 0
    while S:
        x,y = S.popleft()
        count = visit[x][y]+1
        for i in range(4):
            dx = x+dr[i]
            dy = y+dc[i]
            if 0<=dx<row and 0<=dy<col and visit[dx][dy]==-1:
                visit[dx][dy] = count
                S.append((dx,dy))
    return

tc = int(input())
for tc_num in range(tc):
    row, col = map(int,input().split())
    li = list()
    W_li = list()
    visit = [[-1 for c in range(col)]for r in range(row)]
    for i in range(row):
        li.append(list(map(str,input())))
    for x in range(row):
        for y in range(col):
            if li[x][y]=='W':
                visit[x][y] = 0
                W_li.append((x,y))
    dfs(W_li)
    ans = 0
    print(visit)
    for v in visit:
        ans+=sum(v)
    print('#{} {}'.format(tc_num+1,ans))

# 이건 큐쓰니깐 되네 야발