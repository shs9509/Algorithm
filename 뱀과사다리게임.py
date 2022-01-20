#https://www.acmicpc.net/problem/16928

from collections import deque
from operator import ne


sadari, bam = map(int,input().split())
sadari_li = {}
bam_li = {}
li = [0] * 101
visited = [False] * 101
for i in range(sadari):
    a,b = map(int,input().split())
    sadari_li[a]=b
for i in range(bam):
    a,b = map(int,input().split())
    bam_li[a]=b
# print(sadari_li,bam_li)

# count = 0
# for j in range(7,101,6):
#     # print(j)
#     for k in range(j,j+6):
#         if k>101:
#             continue
#         li[k] = min(min(li[k-6:k])+1,li[k])
#         if k in sadari_li:
#             li[sadari_li[k]] = li[k]
#         if k in bam_li:
#             li[bam_li[k]] = li[k]
# print(li,li[101])

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for i in range(1,7):
            next = now+i
            if 0<next<=100 and not visited[next]:
                if next in sadari_li:
                    next = sadari_li[next]
                if next in bam_li:
                    next = bam_li[next]
                if not visited[next]:
                    queue.append(next)
                    visited[next] = True
                    li[next] = li[now] + 1
bfs()
print(li[100])