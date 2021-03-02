#https://www.acmicpc.net/problem/2606
pc = int(input())
link = int(input())
visited = [False for _ in range(pc+1)]
G = [[] for _ in range(pc+1)]
count = 0

for i in range(link):
    u, v = map(int, input().split())
    G[u].append(v)  # G에 연결된 장소 저장
    G[v].append(u)

# print(G)
# print(visited)
visited[1] = True
S = list()
S.append(1)
while S:
    start = S.pop()
    for k in G[start]:
        if visited[k] is False:
            S.append(start)
            visited[k] = True
            S.append(k)
            break
for i in visited:
    if i:
        count += 1
# print(visited)
print(count-1)

