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

def dfs(size,first):
    visit = [0 for _ in range(size+1)]
    S=list()
    S.append(first)
    visit[first] = 1
    while S:
        start = S.pop(0)
        for i in direct[start]:
            if visit[i] == 0:
                S.append(i)
                visit[i] = visit[start] + 1 
    # print(visit)
    return max(visit)-1

num = int(input())
direct = [[] for _ in range(num+1)]
cnt = list()

while True:
    a, b = list(map(int, input().split()))
    if a == -1:
        break
    direct[a].append(b)
    direct[b].append(a)

# print(direct)

for i in range(1,num+1):
    cnt.append(dfs(num,i))

min_value = min(cnt)
print(min_value,cnt.count(min_value))

for i in range(num):
    if min_value == cnt[i]:
        print(i+1, end=' ')





