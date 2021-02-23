# # # some_str='40 50 100 20'
# # # some_list=[440021,23,3,4,5,1]

# # # print(some_list[0])
# # # print(some_str[0])

# # # some_str.split()
# # # # some_list.split()
# # # print(some_str[1].split(),some_str.split()[1],some_str)
# # # print(some_str.split())

# # # some_str.split().sort()

# # # print(some_str.split())
# # # print(some_str)

# # # if 13:
# # #     print('참인가')
# # # else: 
# # #     print('거짓인가.')
# # # if ('M 45')==('M 45'):
# # #     print('참인가')
# # # else: 
# # #     print('거짓인가.')n, m = map(int, input().split())

# # # while True:
# # #      answer = input('0을 입력하지 않으면 끝나지 않습니다.')
# # #      if answer == '0':
# # #           break

# # # for tc in range(1, int(input()) + 1):
# # #     N = int(input())
# # #     # 버스노선정보 저장
# # #     lines = []
# # #     for i in range(N):
# # #         lines.append(list(map(int, input().split())))

# # #     #버스 노선개수 카운트 (정류장번호 -1에 빈도수 저장)
# # #     count = [0]*5000
# # #     for line in lines:
# # #         for dis in range(line[0]-1, line[1]):
# # #             count[dis] += 1

# # #     #물어보는 정류장의 방문 횟수 출력
# # #     P = int(input())
# # #     print('#{}'.format(tc), end=' ')
# # #     for bus_stop in range(P):
# # #         C = int(input())
# # #         print('{}'.format(count[C-1]), end=' ')

# # # [27,35,12,3,4,56,42] > 27부터 시작해서 가장큰 56이 맨뒤에 안착
# # # a= [27,35,12,3,4,56,42] 
# # # for i in range(len(a)-1):
# # #     for j in range(len(a)-i-1):
# # #         if a[j]>a[j+1]:
# # #             a[j+1],a[j]= a[j], a[j+1]
# # # print(a)

# # a= [1,2,2,0,3,3,6,4,3,5]
# # b= [0,0,0,0,0,0,0]
# # e= [0,0,0,0,0,0,0,0,0,0]
# # for i in range(len(a)):
# #     b[a[i]] += 1	# 1의값이면 1의 자리 +1  [c를 만들어가는 과정]
# # for i in range(0,len(b)-1):
# #     b[i+1] += b[i]	# [d를 만들어가는 과정]
# # for i in range (len(a)-1,-1,-1):
# #     e[b[a[i]]-1] = a[i]
# #     b[a[i]] -= 1
# # print(e)

# # # [27,35,12,3,4,56,42] > 27부터 시작해서 가장큰 56이 맨뒤에 안착
# # a= [27,35,12,3,4,56,42] 

# # for i in range(len(a)-1):	#6번 대상을 선정
# #     for j in range(len(a)-i-1):	#뒤에가 점점 차서 비교횟수가 줄어든다. 처음에 6번비교! 그다음 5번!
# #         if a[j]>a[j+1]:
# #             a[j+1],a[j]= a[j], a[j+1]
# # print(a)


# ## 왜안될까....

# N, K = map(int, input().split())
# medal_list = []

# for _ in range(N):
#     medal_list.append(list(map(int, input().split())))

# # 버블정렬 식으로 진행
# for n in range(len(medal_list)):
#     for i in range(len(medal_list)-1):
#         if medal_list[i][1] < medal_list[i+1][1]:       # 금메달이 높은 경우 위치 변경
#             medal_list[i], medal_list[i+1] = medal_list[i+1], medal_list[i]

#         elif medal_list[i][1] == medal_list[i+1][1] and medal_list[i][2] < medal_list[i+1][2]:  # 금메달이 같고, 은메달이 높은 경우 위치 변경
#             medal_list[i], medal_list[i + 1] = medal_list[i + 1], medal_list[i]

#         elif medal_list[i][1] == medal_list[i+1][1] and medal_list[i][2] == medal_list[i+1][2] and medal_list[i][3] < medal_list[i+1][3]:
#             medal_list[i], medal_list[i + 1] = medal_list[i + 1], medal_list[i] # 금, 은메달이 같고 동메달이 높은 경우 위치 변경


# for i in range(len(medal_list) - 1):    # 모든 메달이 같은 상황일 때, 한 인덱스로 모으고 그 뒤 인덱스에 [0, 0, 0, 0] 추가
#     if medal_list[i][1] == medal_list[i+1][1] and medal_list[i][2] == medal_list[i+1][2] and medal_list[i][3] == medal_list[i+1][3]:
#         medal_list[i] = [medal_list[i],medal_list[i+1]]
#         medal_list[i+1] = [0, 0, 0, 0]

# # 정렬 완료된 상황

# for i in range(len(medal_list)):
#     if type(medal_list[i][0]) == int:   # 동순위 상황이 아닌 일반적인 등수일 때
#         if medal_list[i][0] == K:       # 0번 인덱스가 찾던 국가 값과 같으면 +1 하여 출력
#             print(i+1)
#     else:                               # 동순위 상황이라 타입이 list 일 때
#         for medals in (medal_list[i]):  # 리스트 안 리스트를 둘러보면서 0번 인덱스가 찾던 국가 값과 같으면
#             if medals[0] == K:          # +1하여 출력
#                 print(i+1)

# print( int(not 1))
# print( int(not 0))

N = int(input())
total_vote = int(input())
vote_list = list(map(int, input().split())) # input 셋째줄 추천 목록
vote_count = [0] * 101  # 인덱스별 추천 집계 현황
vote_aging = [0] * 101  # 인덱스별 언제 갱신 되었는 지 기록
answer = []

for i in range(total_vote): # 투표별 반복
    min_vote = 987654321  # 최저 추천 횟수 (방출 대상)
    min_aging = 987654321 # 가장 갱신이 오래된 인덱스 (동일 추천 조건 우선 방출 대상)

    for vote_c in vote_count:
        if vote_c >= 1:             # 전체 집계 현황에서 1 이상이면서 min보다 작은 값을 최소 추천으로 갱신
            if vote_c < min_vote:
                min_vote = vote_c

    if vote_count[vote_list[i]] > 0:    # i번째 추천이 기존 집계에 있을 경우 추천수만 증가
        vote_count[vote_list[i]] += 1
        vote_aging[vote_list[i]] = i    # i번째 인덱스 때 갱신했음을 기록 (값이 작을수록 오래된 것)



    elif N >= 1:    # 남아있는 사진틀이 1개 이상일 때 / elif vote_count[vote_list[i]] == 0 and N >= 1도 틀림
        vote_count[vote_list[i]] += 1   # 사진틀을 1개 줄이고 i에 해당하는 카운트와 갱신 기록
        vote_aging[vote_list[i]] = i
        N -= 1

    elif N < 1: # 더 이상 남은 사진틀이 없을 때 / elif vote_count[vote_list[i]] == 0 and N < 1도 틀림
        for j in range(101):                                            # 전체 추천집계와 갱신 시간을 검토
            if vote_count[j] == min_vote and vote_aging[j] < min_aging: # 추천수가 최소일 때의 최소 인덱스 갱신 (방출대상 j)
                min_aging = vote_aging[j]
        for j in range(101):
            if vote_count[j] == min_vote and vote_aging[j] == min_aging: # 방출 대상 j의 추천수를 0으로 초기화
                vote_count[j] = 0                                        # 에이징을 역으로 높은값 987654321로 줘도 틀림
                vote_aging[j] = 0

        vote_count[vote_list[i]] += 1   # 방출 이후 기존 대상 i의 카운트와 갱신 기록
        vote_aging[vote_list[i]] = i
    print(vote_count, vote_aging)

for i in range(len(vote_count)):    # 전체 집계 중 0 이상의 추천 후보자만 오름차순으로 answer 리스트에 추가
    if vote_count[i] > 0:
        answer.append(i)

for ans in answer:
    print(ans, end=" ") # 정답인 각 후보 한칸 씩 띄워가며 출력