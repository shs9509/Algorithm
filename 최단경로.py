# #https://www.acmicpc.net/problem/1753
# import copy
# V, E = list(map(int,input().split()))
# start = int(input())
# node = [[30000 for _ in range(V)] for _ in range(V)]
# for i in range(E):
#     a, b, c = list(map(int,input().split()))
#     node[a-1][b-1] = c

# #[ [0, 2, 3, 0, 0],
# #  [0, 0, 4, 5, 0],
# #  [0, 0, 0, 6, 0],
# #  [0, 0, 0, 0, 0],
# #  [1, 0, 0, 0, 0],


# # print(node)
# tmp = copy.deepcopy(node)

# for i in range(V):
#     for j in range(V):
#         if j==i:
#             continue
#         for k in range(V):
#             if k==i or k==j:
#                 continue
#             tmp[j][k] = min(tmp[j][k], tmp[j][i]+tmp[i][k])

# # print(tmp)
# for i in range(len(tmp[start-1])):
#     if i == start-1:
#         print(0)
#     elif tmp[start-1][i] == 30000:
#         print("INF")
#     else:
#         print(tmp[start-1][i])


###################### v플로이드 와샬 안되..

import sys
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split()) # 5 ,6
k = int(sys.stdin.readline()) # 1 (start)
s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []

def dijkstra(start):
    dp[start] = 0 # dp[1] = 0 (시작점은 0처리)
    heappush(heap, [0, start]) # heap =[0,1]
    while heap:
        w, n = heappop(heap) # w=0 n=1
        for n_n, wei in s[n]: # s[1] = [[2, 2], [3, 3]]  (n_n=2, wei=2)
            n_w = wei + w # 2+0 = n_w
            if n_w < dp[n_n]: # if 2<dp[2]
                dp[n_n] = n_w # dp[2] = 2   //  dp[3] = 3
                heappush(heap, [n_w, n_n]) # heap [2,2]  [3,3]
        print(heap)
        print(dp)

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
print(s)
#[[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]
dijkstra(k)
for i in dp[1:]:
    print(i if i != inf else "INF")