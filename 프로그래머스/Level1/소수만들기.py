# https://programmers.co.kr/learn/courses/30/lessons/12977
import math

# 소수 판별 함수(에라토스테네스의 체)
def sosu(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return array[-1]
  
def solution(nums):
    tmp=[]
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1,len(nums)):
                tmp.append(nums[i]+nums[j]+nums[k])
    answer =0
    for t in tmp:
        if sosu(t):
            answer+=1

    return answer