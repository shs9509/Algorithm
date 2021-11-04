# https://www.acmicpc.net/problem/2559

# 느린 답
N, K = map(int, input().split())
li = list(map(int, input().split()))
result = list()
for i in range(0,len(li)-K):
    result.append(sum(li[i:i+K]))
print(max(result))



# 빠른 답
N, K = map(int, input().split())
li = list(map(int, input().split()))
sum_val = sum(li[:K])
result = [sum_val]

for i in range(0, len(li)-K):
    sum_val = sum_val - li[i] + li[i+K]
    result.append(sum_val)
print(max(result))