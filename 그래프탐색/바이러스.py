# https://www.acmicpc.net/problem/2606

N = int(input())
M = int(input())
li = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    li[s].append(e)
    li[e].append(s)

visited = [False] * (N+1)

def dfs():
    lis=[1]
    while(lis):
        S = lis.pop(0)
        for j in li[S]:
            if visited[j]==False:
                lis.append(j)
                visited[j] = True
            else:
                continue

dfs()
# print(visited)
print(visited.count(True)-1)