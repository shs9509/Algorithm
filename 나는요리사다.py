#https://www.acmicpc.net/problem/2953

score = list()  # 점수 저장
score_sum = list()  # 점수의 합
for i in range(5):
    score.append(list(map(int,input().split())))
for j in score:
    score_sum.append(sum(j))

max_val=score_sum[0]

for k in range(5):
    if score_sum[k]>= max_val:  # if score_sum[k]>= max_val: '=' 이거 안하면 틀림 왜? 
        max_val = score_sum[k]	# 최대값이안변하면 그거는 그거대로 오류
        max_id = k+1

print('{} {}'.format(max_id,max_val))


# if score_sum[k]>= max_val: '=' 이거 안하면 틀림 왜? 해결!