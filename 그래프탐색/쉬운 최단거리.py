# https://www.acmicpc.net/problem/14940

n,m = map(int,input().split())

li = list()
for i in range(n):
    li.append(list(map(int,input().split())))
for x in range(n):
    for y in range(m):
        if li[x][y]==2:
            start_x =x
            start_y =y

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited = [[False for _ in range(m)] for _ in range(n)]

def dfs():
    tmp=[(start_x,start_y)]
    li[start_x][start_y]=0
    visited[start_x][start_y]= True
    while(tmp):
        x,y = tmp.pop(0)
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0<=X<n and 0<=Y<m and visited[X][Y]==False:
                if li[X][Y] ==0:
                    continue
                elif li[X][Y] ==1:
                    tmp.append((X,Y))
                    visited[X][Y]=True
                    li[X][Y] = li[x][y]+1
dfs()
for x in range(n):
    for y in range(m):
        if visited[x][y] == False and li[x][y]!=0:
            li[x][y] = -1
for i in range(n):
    print(' '.join(map(str,li[i])))


