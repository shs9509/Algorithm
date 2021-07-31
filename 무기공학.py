#https://www.acmicpc.net/problem/18430
## 어려운거같은디..
r,c = list(map(int,input().split()))
li = list()
for i in range(c):
    li.append(list(map(int,input().split())))

visit = [ [True for _ in range(c)] for _ in range(r) ]

one =[[1,0],[1,0],[-1,0],[-1,0]]
two =[[0,1],[0,-1],[0,-1],[0,1]]

result =[0]

def dfs(x,y,v,value):
    result.append(value)
    for i in range(4):
        X1 = x+one[i][0]
        Y1 = y+one[i][1]
        X2 = x+two[i][0]
        Y2 = y+two[i][1]
        if 0<=X1<r and  0<=X2<r and 0<=Y1<r and 0<=Y2<r and v[X1][Y1] and v[X2][Y2] and v[x][y]:
            v[X1][Y1] = False
            v[X2][Y2] = False
            v[x][y] = False
            if 0<=y+1<c:
                dfs(x,y+1,v,value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
            else:
                if 0<=x+1<r:
                    dfs(x+1,y+1-c,v,value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
                else:
                    result.append(value+li[x][y]*2 + li[X1][Y1] + li[X2][Y2])
                    return
        else:
            if 0<=y+1<c:
                dfs(x,y+1,v,value)
            else:
                if 0<=x+1<r:
                    dfs(x+1,y+1-c,v,value)
                else:
                    result.append(value)
                    return

dfs(0,0,visit,0)
print(result) 