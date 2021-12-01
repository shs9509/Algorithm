#https://www.acmicpc.net/problem/1912
n = int(input())

li = list(map(int, input().split()))
result = [0] * len(li)
result[0] = li[0]

for i in range(1, len(li)):
    result[i] = max(li[i], result[i-1] + li[i])

print(max(result))