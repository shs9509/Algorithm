#https://www.acmicpc.net/problem/2660

'''
DFS 문제 아님?
너와나의 연결고리 체크하고 1이 몇명 연결되어있는지
2가 몇명 연결되어있는지
결국 마지막에 for문 돌려서 최소값 구하기

근데 친구의 친구가 2이고
친구의 친구의 친구가 3인거면
BFS다.
'''

def bfs(size,first):    # 사람수, 그래프의 시작지점
    visit = [0 for _ in range(size+1)]
    S=list()
    S.append(first)
    visit[first] = 1
    while S:
        start = S.pop(0)
        for i in direct[start]: 
            if visit[i] == 0:
                S.append(i)
                visit[i] = visit[start] + 1 # 방문하면서 start가 가지고있던 친구거리 값을 +1 한다.
    return max(visit)-1

num = int(input())  # 사람수
direct = [[] for _ in range(num+1)] # 연결 그래프
cnt = list()    # 최대 친구 거리수 저장리스트

while True:
    a, b = list(map(int, input().split())) 
    if a == -1:
        break
    direct[a].append(b)
    direct[b].append(a) # 양방향으로 친구를 리스트에 등록한다.


for i in range(1,num+1):    # 각 사람마다 시작지점으로 그래프를 탐색한다.
    cnt.append(bfs(num,i))

min_value = min(cnt)    #  친구 최소거리값
print(min_value,cnt.count(min_value)) # 친구 최소거리값과 그 값을 가진 사람수

for i in range(num):    # 최소값을 가진 사람 출력
    if min_value == cnt[i]:
        print(i+1, end=' ')





