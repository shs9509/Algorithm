#https://www.acmicpc.net/problem/2846

step_num = int(input()) # 계단 수
step_height = list(map(int,input().split()))    # 계단 높이
step_gap = 0    # 오르막길 높이
step_gaps = list()  # 오르막길 높이들
for j in range(len(step_height)-1):
    if step_height[j] >= step_height[j+1]:
        # step_gaps.append(step_gap) 이렇게 하면 마지막 부분이 오르막길이면 append 되지 않음
        step_gap = 0
    else:
        step_gap += (step_height[j+1] - step_height[j]) # 오르막길이면 계속 높이를 더해줌
    step_gaps.append(step_gap)
        
print(max(step_gaps))

# 끝에 [0]을 넣어줌으로서 간단해짐 -> 마지막 부분이 오르막길이면 append 되지 않음 상태를 막을수잇다.