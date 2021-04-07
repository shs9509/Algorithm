#https://www.acmicpc.net/problem/2210
#https://claude-u.tistory.com/433
'''
어쨰 비효율적인 방법밖에 생각이 안난다.
5번만 움직이니깐 그렇게 비효율적인건 아닌가?

'''

def dfs(x,y,number):
    if len(number)==6:
        if number not in tmp:
            tmp.append(number)
        return

    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,number+li[nx][ny])

li= list()
store = list()
dr = [0,0,-1,1]
dc = [1,-1,0,0]
tmp = list()
for i in range(5):
    li.append(list(map(str, input().split())))


for x in range(5):
    for y in range(5):
        dfs(x,y,li[x][y])

print(len(tmp))

