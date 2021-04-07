#https://www.acmicpc.net/problem/2644
'''
이거 걍 bfs 그래프문제 아닌가?
'''
def bfs(start,end):
    visit = [0 for _ in range(num+1)]
    S=list()
    S.append(start)
    visit[start] =1
    count = 0
    while S:
        start = S.pop(0)
        count = visit[start]### 이거떄매 시간을 얼매네 난린거여
        count += 1 
        for j in save[start]:
            if j == end:
                visit[end] = count-1
                return visit[end]
            if visit[j]== 0:
                visit[j] = count
                S.append(j)       
           
    return -1

num = int(input())
a, b = map(int, input().split())
E = int(input())
save = [[] for _ in range(num+1)]
for i in range(E):
    c,d = map(int,input().split())
    save[c].append(d)
    save[d].append(c)
# print(save)
print(bfs(a,b))




