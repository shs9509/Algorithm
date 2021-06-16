#https://www.acmicpc.net/problem/17626
N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 99999999
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])
# 이방법 아무리생각해도 시간초과인데 pypy는 통과함 어쩔수없는듯?