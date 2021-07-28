#https://www.acmicpc.net/problem/16954

li =list()
li.append('........')
for i in range(8):
    li.append(input())
# print(li)

wall = []
for r in range(9):
    for c in range(8):
        if li[r][c]=='#':
            wall.append([r,c]) 

dr=[-1,0,-1,0,-1,0,1,1,1]
dc=[0,1,1,-1,-1,0,0,1,-1]
visit = [[True for j in range(8) ] for j in range(9) ]

S = [(8,0)]

def dfs():
    flag= False
    while S:
        # print(wall)
        a = len(S)
        for v in range(a):
            x, y =S.pop(0)
            for k in range(9):
                X = x + dr[k]
                Y = y + dc[k]
                if 1<=X<9 and 0<=Y<8 and visit[X][Y]:
                    # print(wall)
                    if [X,Y]==[1,7]:
                        flag=True
                        break
                    if ([X-1,Y] in wall) or ([X,Y] in wall):
                        continue
                    else:
                        S.append([X,Y])  
                        visit[X][Y]= False
        for n in range(len(wall)):
            wall[n][0] +=1
        # print(S)
        if flag:
            break
    if flag:
        return 1
    else:
        return 0
        
print(dfs())

# 이거 재귀로 해야되네