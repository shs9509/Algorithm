# #https://www.acmicpc.net/problem/1238
# # 4 8 2 //4명의 학생, 8개의 다리 2번에서 모임
# # 다익스트라인데 시작에서 가서 다시 돌아오는거 계산


# import sys
# from heapq import heappush, heappop
# inf = 100000000
# v, e, k = map(int, sys.stdin.readline().split()) # 5 ,6
# s = [[] for _ in range(v + 1)]
# dp = [inf] * (v + 1)
# heap = []

# def dijkstra(start,end):
#     dp = [inf] * (v + 1)
#     dp[start] = 0 # dp[1] = 0 (시작점은 0처리)
#     heappush(heap, [0, start]) # heap =[0,1]
#     while heap:
#         w, n = heappop(heap) # w=0 n=1
#         for n_n, wei in s[n]: # s[1] = [[2, 2], [3, 3]]  (n_n=2, wei=2)
#             n_w = wei + w # 2+0 = n_w
#             if n_w < dp[n_n]: # if 2<dp[2]
#                 dp[n_n] = n_w # dp[2] = 2   //  dp[3] = 3
#                 heappush(heap, [n_w, n_n]) # heap [2,2]  [3,3]
#         print(heap)
#         print(dp)
#     print(dp[end])

# for i in range(e):
#     u, v, w = map(int, sys.stdin.readline().split())
#     s[u].append([v, w])
# print(s)
# #[[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]
# dijkstra(1,k)
# dijkstra(k,1)


import sys
import copy
import heapq
from collections import deque
input=sys.stdin.readline
inf=2**32

def bfs(start,end): 
   heap=[]
   heapq.heappush(heap,[dist[start],start]) # heap 에 [0,1]
   while heap:
      weight,cur=heapq.heappop(heap) #[0,1]  cur 1은 현 지점, weight은 거리
      if cur==end:return weight # 현지점이 끝이다? 그럼 거리를 꺼내셈
      for to,cost in arr[cur]: # arr에는 이미 갈수있는 거리가 저장되있음  to는 갈수있는곳, cost는 그에대한 비용
         if dist[to]>dist[cur]+cost: # dist[cur] 는 지금까지의 거리 근데 넘어가려면 cost를 더하는데 그럼 이미 가있는 곳과 비교를 해야됨
            dist[to]=dist[cur]+cost
            heapq.heappush(heap,[dist[to],to]) # 그럼3에 도착하는게 새로 생김 그럼 길이생긴거니 거기 heap에 추가가됨
   return inf


n,m,x=map(int,input().split()) # 값을 받고
arr={i:[] for i in range(1,n+1)}

for _ in range(m): # 값을 넣고
   a,b,c=map(int,input().split())
   arr[a].append([b,c])
   
res =[]
for start in range(1,n+1):
   dist=[inf]*(n+1) # 거리 저장할 list
   dist[start]=0
   res.append(bfs(start,x)) #start~ x

for end in range(1,n+1):
   dist=[inf]*(n+1)
   dist[x]=0
   res[end-1]+=bfs(x,end)

print(max(res))