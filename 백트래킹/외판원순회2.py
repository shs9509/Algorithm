#0620 외판원 순회 2 : https://www.acmicpc.net/problem/10971

def travel(start,f,v,c,count):
    v[start]=True
    global min_cost
    if c >= min_cost:
        return
    if count==n-1:
        if li[f][start]:
            c+=li[f][start]
            if min_cost>=c:
                min_cost = c
        return
    else:
        for i in range(n):
            if v[i]==False and li[f][i]:
                v[i]=True
                travel(start,i,v,c+li[f][i],count+1)
                v[i]=False



n = int(input())
li = list()
for i in range(n):
    li.append(list(map(int,input().split())))

min_cost=99999999999
for s in range(n):
    cost =0
    visit = [False for _ in range(n)]
    travel(s,s,visit,cost,0)
print(min_cost)