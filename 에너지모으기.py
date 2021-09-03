#https://www.acmicpc.net/problem/16198
#168ms
import copy
n = int(input())
li = list(map(int,input().split()))

result = list()
def dfs(l,val):
    if len(l)==2:
        result.append(val)
        return
    else:
        for i in range(1,len(l)-1):
            lis = copy.copy(l)
            lis.pop(i)
            dfs(lis,val+(l[i-1]*l[i+1]))

dfs(li,0)

print(max(result))