# https://www.acmicpc.net/problem/16234

import copy


N,L,R = map(int,input().split())
li = list()
for i in range(N):
    li.append(list(map(int,input().split())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_count =0
while(True):
    if move_count >2000:
        break
    visited = [[False for _ in range(N)] for _ in range(N)]
    tmp_li = copy.deepcopy(li)
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            else:
                tmp = [(x,y)]
                tmp_pos = [(x,y)]
                count = 1
                value = li[x][y]
                visited[x][y]=True
                while(tmp):
                    ax,ay =tmp.pop(0)
                    for i in range(4):
                        X = ax+dx[i]
                        Y = ay+dy[i]
                        if 0<=X<N and 0<=Y<N and L<=abs(li[ax][ay]-li[X][Y])<=R and visited[X][Y]==False:
                            tmp.append((X,Y))
                            tmp_pos.append((X,Y))
                            count+=1
                            value+=li[X][Y]
                            visited[X][Y]=True
                # print(tmp_pos,value,count)
                for j in tmp_pos:
                    b_x,b_y = j
                    li[b_x][b_y] = value//count
                    # print('no',li)
    if tmp_li == li:
        break
    # print(li)
    move_count +=1
# print(li)
print(move_count)