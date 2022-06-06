# import itertools

# def solution(jobs):
#     orders = [a for a in range(len(jobs))]
#     disc_orders = list(itertools.permutations(orders, len(jobs)))
#     # print(disc_orders)
#     answer = []
#     for disc_order in disc_orders:
#         count=0
#         last=jobs[disc_order[0]][0]
#         for order in disc_order:
#             count+= jobs[order][1] + abs(jobs[order][0]-last)
#             last+= jobs[order][1]
#             # print(count)
#         answer.append(count//len(jobs))
#     return min(answer)

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)


# 힙큐 안 쓴 버전
def solution(jobs):
    disc_length = len(jobs)
    answer=0
    jobs.sort(key=lambda x:(x[0],x[1]))
    start, end= [0,jobs[0][0]+jobs[0][1]]
    count = jobs[0][1]
    jobs.pop(0)
    tmp_jobs=[]
    while(jobs or tmp_jobs):
        for idx in range(len(jobs)):
            if start <= jobs[idx][0] <= end:
                tmp_jobs.append(jobs.pop(idx))
                break
        else:
            tmp_jobs.sort(key=lambda x:(x[1],x[0]))
            if tmp_jobs:
                wait_start, length =  tmp_jobs.pop(0)
                end+=length
                count+= (end-wait_start)
            else:
                end+=1
    return count//disc_length