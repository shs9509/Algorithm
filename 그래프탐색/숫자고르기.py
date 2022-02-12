# https://www.acmicpc.net/problem/2668

from tabnanny import check


N = int(input())
li = [0]
for i in range(N):
    li.append(int(input()))
# print(li)
visited = [False for _ in range (N+1)]
max_count = 0
max_count_li = []

def dfs(start):
    tmp = [start]
    count =[start]
    check = False
    while(tmp):
        s = tmp.pop()
        if visited[li[s]]==False:
            if li[s]== start:
                check = True
                visited[li[s]] = True
                break
            tmp.append(li[s])
            visited[li[s]] = True
            count.append(li[s])
    if check:
        return count
    else:
        for i in count:
            visited[i]=False
        return 


ans =[]

for s in range(1,N+1):
    if visited[s] ==True:
        continue
    if li[s] == s:
        ans.append(s)
        continue
    part_ans = dfs(s)
    if part_ans:
        for i in part_ans:
            ans.append(i)
ans.sort()

print(len(ans))
for i in ans:
    print(i)