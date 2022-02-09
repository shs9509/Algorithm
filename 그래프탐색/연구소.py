# https://www.acmicpc.net/problem/14502
import copy

x,y = map(int,input().split())
li= list()
for i in range(x):
    li.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

virus = []
wall = []
vacant = []
min_count = 10000000000
for j in range(x):
    for k in range(y):
        if li[j][k] == 2:
            virus.append((j,k))
        elif li[j][k] ==1:
            wall.append((j,k))
        else:
            vacant.append((j,k))
length = len(vacant)
# print(len(vacant))
def dfs(min_val):
    tmp_virus = copy.deepcopy(virus)
    count =len(tmp_virus)
    tmp_li = copy.deepcopy(li)
    # print(tmp_li)
    # print(tmp_virus,tmp_li)
    visited = [[False for _ in range(y)] for _ in range(x)]
    # print(visited)
    while(tmp_virus):
        a,b = tmp_virus.pop(0)
        if count >= min_val:
            return
        for i in range(4):
            X = a+dx[i]
            Y = b+dy[i]
            if 0<=X<x and 0<=Y<y and tmp_li[X][Y]==0 and visited[X][Y]==False:
                tmp_virus.append((X,Y))
                tmp_li[X][Y]=2
                count+=1
                visited[X][Y]=True
    # print(tmp_li)
    # print(count)
    return count


ans=[]
for i in range(length-2):
    li[vacant[i][0]][vacant[i][1]] =1
    for j in range(i+1,length-1):
        li[vacant[j][0]][vacant[j][1]] =1
        for k in range(j+1,length):
            li[vacant[k][0]][vacant[k][1]] =1
            val = dfs(min_count)
            if val:
                ans.append(val)
                min_count = min(min_count,val)        
            li[vacant[k][0]][vacant[k][1]] =0
        li[vacant[j][0]][vacant[j][1]] =0
    li[vacant[i][0]][vacant[i][1]] =0

print(x*y-min(ans)-len(wall)-3)
# print(ans)    

