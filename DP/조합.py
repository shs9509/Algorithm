#https://www.acmicpc.net/problem/2407

import math

n, m = map(int, input().split())

x = math.factorial(n)
y = (math.factorial(n-m)) * (math.factorial(m))

answer = x//y

print(answer)