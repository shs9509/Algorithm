#https://www.acmicpc.net/problem/1325

N,M = map(int,input().split())

li = [[] for _  in range(N+1)]
for i in range(M):
    FROM,TO = map(int,input().split())
    li[TO].append(FROM)

# print(li)

def dfs(s):
    lis = [s]
    count = 0
    while lis:
        pos =  lis.pop()
        visited[pos] = True
        count +=1
        for k in li[pos]:
            if visited[k] == False:
                visited[k] = True
                lis.append(k)

    return count
    
ans = list()
for j in range(1,N+1):
    visited = [False]*(N+1)
    ans.append(dfs(j))

def max_idx(li):
    max_li = []
    max_val = 0
    for i in range(len(li)):
        if max_val<li[i]:
            max_li = []
            max_li.append(i+1)
            max_val=li[i]
        elif max_val==li[i]:
            max_li.append(i+1)
    return " ".join(map(str,max_li))

# print(ans)
print(max_idx(ans))