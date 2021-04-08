#https://www.acmicpc.net/problem/2210
#https://claude-u.tistory.com/433
'''
어쨰 비효율적인 방법밖에 생각이 안난다.
5번만 움직이니깐 그렇게 비효율적인건 아닌가?

'''

def dfs(x,y,number):# 시작지점과 경로(number)를 인자로 받는다.
    if len(number)==6: # 만약 number가 6자리면
        tmp.append(number)  # tmp에 넣어준다.
        return

    for i in range(4): # 사방탐색해서 경로를만든다.
        nx = x + dr[i]
        ny = y + dc[i]
        if 0<=nx<5 and 0<=ny<5: # 숫자판을 넘지않는다면 dfs를 돌려서 다음경로를 찾는다.
            dfs(nx,ny,number+li[nx][ny]) # li[nx][ny]를 다음경로로 추가해준다.
                                         # 이과정을 계속하면 number에 경로가 쌓인다. 

li= list() # 숫자판
dr = [0,0,-1,1] # 사방탐색을 위한 재료
dc = [1,-1,0,0]
tmp = list()    # 6번의 경로들이 저장되는 곳
for i in range(5):
    li.append(input().split())


for x in range(5):
    for y in range(5): # 시작지점 x,y를 지정해서 dfs 를 돌린다.
        dfs(x,y,li[x][y])


print(len(set(tmp))) # 중복된경로를 없애기 위해서 set을 써준다.

