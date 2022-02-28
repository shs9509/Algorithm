# https://www.acmicpc.net/problem/11725

N= int(input())
li = [ [] for m in range(N+1)]
parent = [ 0 for _ in range(N+1)]
check = [ False for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
# print(li)g
tmp =[1]
while(tmp):
    t = tmp.pop()
    check[t]=True
    for j in li[t]:
        if check[j]==False:
            parent[j] = t
            tmp.append(j)
            check[j]=True

for k in range(2,len(parent)):
    print(parent[k])