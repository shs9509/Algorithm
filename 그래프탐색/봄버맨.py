#https://www.acmicpc.net/problem/16918

# 시간
def bomb(l,sec):
    if sec ==0:
        sec+=1
        for x in range(R):
            for y in range(C):
                if l[x][y]==3:
                    l[x][y]=2
        bomb(l,sec)
    elif sec == N:
        return
    else:
        sec+=1
        s=list()
        for x in range(R):
            for y in range(C):
                if l[x][y]==1:
                    s.append((x,y))
        for x in range(R):
            for y in range(C):
                if l[x][y]==3:
                    l[x][y]=2
                elif l[x][y]==2:
                    l[x][y]=1
                elif l[x][y]==0:
                    l[x][y]=3
        for (x,y) in s:
            for i in range(5):
                X = x+dr[i]
                Y = y+dc[i]
                if 0<=X<R and 0<=Y<C:
                    l[X][Y]=0
        bomb(l,sec)
        

dr=[0,0,0,-1,1]
dc=[0,1,-1,0,0]
R,C,N = map(int,input().split())
li = list()
for i in range(R):
    li.append(list(input()))
for x in range(R):
    for y in range(C):
        if li[x][y]=='.':
            li[x][y]=0
        else:
            li[x][y]=3
bomb(li,0)
for x in range(R):
    for y in range(C):
        if li[x][y]==0:
            print('.',end='')
        else:
            print('O',end='')
    print('')
