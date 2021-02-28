#https://www.acmicpc.net/problem/1713
def min_idx(li):
    min_val = 1000
    min_id = 0
    for i in range(len(li)-1,-1,-1):
        if min_val>=li[i]: 
            min_id= i
            min_val =li[i]
    return min_id           #최소값 인덱스구하기


frame_num = int(input()) #액자개수 3
reco_time = int(input()) #추천횟수  9
stu_li = list(map(int,input().split()))  #학생의 추천리스트 [2,1,4,3,5,6,2,7,2]
frame = list() 
count_num = [0]*frame_num   #기존 액자의 추천수 [0,0,0]

for i in range(reco_time):
    if len(frame) < frame_num and stu_li[i] not in frame:   # 1. 액자가 꽉차지않고 없는 추천이 들어올 경우
        frame.append(stu_li[i])         # 액자에 추천번호 추가 
        pos = frame.index(stu_li[i])    # 추천번호의 위치
        count_num[pos] += 1             # 그 위치의 추천수 +1
    
    elif stu_li[i] in frame:    # 2. 기존 액자에 있는 추천번호가 들어올 경우
        pos = frame.index(stu_li[i])
        count_num[pos] += 1     # 추천수 +1
    
    else:                       # 3. 새로운 추천이 들어올 경우
        frame.pop(min_idx(count_num))   # 추천수가 가장 작은 자리의 액자를 뽑아냄
        count_num.pop(min_idx(count_num))   # 추천수도 뽑아내기
        frame.append(stu_li[i])     # 새로 넣기
        count_num.append(1)
    # print(frame , count_num)

for j in sorted(frame):
    print(j, end=' ')



        # print(count_num,'count_num')
# frame = list()
# count_num = list()
# for i in range(reco_time):
#     min_id = min_idx(frame)
#     old = min_idx(count_num)
#     if len(frame)<frame_num:
#         frame.append(stu_li[i])
#         count_num.append(i)
#         # print(count_num,'count_num')
#     else:
#         if frame.count(frame[min_id]) > 1:
#             a = list()
#             for j in range(len(frame)): # 0 1 2
#                 if frame[j] == frame[min_id]:   # 최소값과 같은 자리를 
#                     a.append(j)                 # 리스트에 넣어줌 [1,2]
#                 # print(a)
#             b = list()
#             for k in a:
#                 b.append(count_num[k])
#             # print(b)
#             # print(count_num,'count_num')
#             h = min(b) # 그자리의 나이(age)를 확인min_idx([count_num[1],count_num[2]])
#             frame.pop(h)
#             frame.insert(h,stu_li[i])  # 가장작은거 빼고 그자리에 넣기
#             count_num.pop(h)
#             count_num.insert(h,i)    
#             # print(count_num,'count_num')

#         else:
#             frame.pop(min_id)
#             frame.insert(min_id,stu_li[i])  # 가장작은거 빼고 그자리에 넣기
#             count_num.pop(min_id)
#             count_num.insert(min_id,i)
#             # print(count_num,'count_num')
#         # print(frame)
# for i in frame:
#     print(i, end=' ')
'''
 update 쓰려고 했는데 보니깐 원소를 여러개 추가할때 update를 쓴다
 ex) s1.update([4,5,6])
 replace쓰려고 햇는데 생각해보니깐 그러면 최소가 여러개면 다바뀜
 아 오래된거 먼저인데 이게 또 문제네
 아 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
 지랄 개지랄!
 명세서 꼭 자세히 보자 씨발!!!!!!!!!!!!!!!
'''