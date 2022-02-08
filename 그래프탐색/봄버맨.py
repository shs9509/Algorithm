#https://www.acmicpc.net/problem/16918

# 시간
# def bomb(l,sec):
#     if sec ==0:
#         sec+=1
#         for x in range(R):
#             for y in range(C):
#                 if l[x][y]==3:
#                     l[x][y]=2
#         bomb(l,sec)
#     elif sec == N:
#         return
#     else:
#         sec+=1
#         s=list()
#         for x in range(R):
#             for y in range(C):
#                 if l[x][y]==1:
#                     s.append((x,y))
#         for x in range(R):
#             for y in range(C):
#                 if l[x][y]==3:
#                     l[x][y]=2
#                 elif l[x][y]==2:
#                     l[x][y]=1
#                 elif l[x][y]==0:
#                     l[x][y]=3
#         for (x,y) in s:
#             for i in range(5):
#                 X = x+dr[i]
#                 Y = y+dc[i]
#                 if 0<=X<R and 0<=Y<C:
#                     l[X][Y]=0
#         bomb(l,sec)
        

# dr=[0,0,0,-1,1]
# dc=[0,1,-1,0,0]
# R,C,N = map(int,input().split())
# li = list()
# for i in range(R):
#     li.append(list(input()))
# for x in range(R):
#     for y in range(C):
#         if li[x][y]=='.':
#             li[x][y]=0
#         else:
#             li[x][y]=3
# bomb(li,0)
# for x in range(R):
#     for y in range(C):
#         if li[x][y]==0:
#             print('.',end='')
#         else:
#             print('O',end='')
#     print('')

# 0초 (폭탄한개) -> 1초 -> 2초(설치안된곳에 설치)->3초(맨처음 설치한거 뻥)

X,Y,s = map(int,input().split())
li = list()
for i in range(X):
    li.append(list(input()))
# print(li)

bomb=[]
for x in range(X):
    for y in range(Y):
        if li[x][y]=='O':
            bomb.append((x,y))

dx = [1,-1,0,0,0]
dy = [0,0,1,-1,0]
bomb_li = [[-1 for _ in range(Y)] for _ in range(X)]
now =1

def tranfer_ans(li):
    for x in range(X):
        for y in range(Y):
            if li[x][y] == -1:
                li[x][y] = '.'
            else:
                li[x][y] = 'O'

for bom in bomb:
    a,b=bom
    bomb_li[a][b]=3

for x in range(X):
    for y in range(Y):
        if bomb_li[x][y]==-1:
            continue
        else:
            bomb_li[x][y]-=1
if s==1:
    tranfer_ans(bomb_li)
    for i in bomb_li:
        print(''.join(i))

if s>1:
    while True:
        now+=1
        tmp_bomb =[]
        for x in range(X):
            for y in range(Y):
                if bomb_li[x][y]==-1:
                    bomb_li[x][y]=3
                else:
                    bomb_li[x][y]-=1
                    if bomb_li[x][y]==1:
                        tmp_bomb.append((x,y))
        if now ==s:
            break
        now +=1
        for bomb in tmp_bomb:
            bomb_x, bomb_y = bomb
            for j in range(5):
                Bomb_x = bomb_x+ dx[j]
                Bomb_y = bomb_y+ dy[j]
                if 0<=Bomb_x<X and 0<=Bomb_y<Y:
                    bomb_li[Bomb_x][Bomb_y]=-1
        for x in range(X):
            for y in range(Y):
                if bomb_li[x][y] != -1:
                    bomb_li[x][y]-=1
        if now ==s:
            break

    # print(bomb_li)
    tranfer_ans(bomb_li)
    for i in bomb_li:
        print(''.join(i))



