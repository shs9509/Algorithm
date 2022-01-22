N, M, S = list(map(int, input().split()))

li=[[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    FROM, TO = map(int,input().split())
    li[FROM].append(TO)
    li[TO].append(FROM)
for j in range(N+1):
    li[j].sort()

# print(li)
dfs_ans= []
bfs_ans= []
def dfs(s):
    dfs_li = [s]
    visited[s]= True
    while dfs_li:
        pos = dfs_li.pop()
        dfs_ans.append(pos)
        if li[pos]:
            for k in li[pos]:
                if not visited[k]:
                    visited[k]=True
                    dfs(k)


def bfs(s):
    bfs_li = [s]
    visited[s]= True
    while bfs_li:
        pos = bfs_li.pop(0)
        bfs_ans.append(pos)
        if li[pos]:
            for k in li[pos]:
                if not visited[k]:
                    visited[k]=True
                    bfs_li.append(k)

dfs(S)
visited = [False] * (N+1)
bfs(S)

print(' '.join(map(str,dfs_ans)))
print(' '.join(map(str,bfs_ans)))


