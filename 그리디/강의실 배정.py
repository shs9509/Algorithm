#0708 강의실 배정 : https://www.acmicpc.net/problem/11000

# tc = int(input())
# li = list()
# for i in range(tc):
#     li.append(list(map(int,input().split())))

# result_li = list()

# for j in li:
#     start,end = j
#     for k in range(start,end):
#         result_li.append(k)

# result_li=sorted(result_li)
# count =1
# max_count = 0
# for k in range(len(result_li)-1):
#     if result_li[k] == result_li[k+1]:
#         count+=1
#     else:
#         if count >= max_count:
#             max_count =count
#             count=1
#         else:
#             count = 1

# print(max_count)

###########################
# result_li = list()

# for j in li: # j [2,4]
#     start,end = j # 2,4
#     for k in result_li: # k = [1,2] [2,1]
#         if start<=k[0]<end:
#             k[1]+=1
#     result_li.append([start,1])
#     result_li.append([end,0])

# # print(result_li)

# max_count = 0
# for m in result_li:
#     if m[1]>= max_count:
#         max_count = m[1]
# print(max_count)

# [2,4] [3,5] [2,7]

# [0,0,0,0,0,0,0]
# [[2,2] [3,2] [4,2] [7,0]] 

#########################
import sys
import heapq

input = sys.stdin.readline
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]

# '수업 시작 시간' 기준으로 오름차순 정렬
lessons = sorted(lessons, key=lambda x: x[0])
print(lessons)
q = []
for lesson in lessons:
    # 이전 수업이 끝나는 시간과 다음 수업이 시작하는 시간을 비교
    if q and q[0] <= lesson[0]:
        heapq.heappop(q)
    heapq.heappush(q, lesson[1])
    print(q)

# 큐의 각각 원소는 한 강의실에서 하나의 수업이 진행중이라고 생각하면 쉽다.
# 즉, 큐의 사이즈가 강의실의 개수가 된다.
print(len(q))

## 그냥은 못쓰나??