# https://www.acmicpc.net/problem/22862
# https://velog.io/@harryyyyy/%EB%B0%B1%EC%A4%80-22862-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A7%9D%EC%88%98-%EC%97%B0%EC%86%8D%ED%95%9C-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

#수열 S에서 최대 K번 원소를 삭제한 수열에서 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 출력한다.
# 빼고 더하면서 진행하면 될듯

# N, M = map(int,input().split())
# li = list(map(int,input().split())) #1 2 3 4 5 6 7 8
# s= 0
# delete_count =0
# max_length = 0
# length =0
# for i in range(N):
#     if li[i]%2==1:
#         delete_count+=1
#         if delete_count==M:
#             count =0
#             while(True):
#                 if count >=1 and li[s]%2==0:
#                     break
#                 if li[s]%2==1:
#                     count+=1
#                 else:
#                     length-=1
#                 s+=1
#             delete_count-=count
#             if delete_count <0:
#                 delete_count=0
#         # print(s,'sss')
    
#         if max_length < length:
#                 max_length = length
#     else:
#         length+=1
#         if max_length < length:
#                 max_length = length
#     # print(length)

# print(max_length)

N, K = map(int, input().split())
li = list(map(int, input().split()))

end_point = 0 # 끝 포인터
max_lenght = 0 # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
length = 0 # 현재 짝수 부분 수열의 길이
count = 0 # 지우려는 홀수 카운트

# start를 N 까지 계속 증가시키며 반복
for start in range(N):
    
    # end를 가능한 만큼 이동
    while (count <= K and end_point < N):     
        
        if li[end_point] % 2 == 1: # 홀수
            count += 1
        else: # 짝수
            length += 1
        end_point += 1 # 끝 점 이동
        
        if start == 0 and end_point == N:
            max_lenght = length
            break
        
    if count == K+1 :
        max_lenght = max(length, max_lenght)
        
    if li[start] %2 == 1: # 시작점이 홀수
        count -= 1
    else: # 시작점이 짝수
        length -= 1
        
print(max_lenght)