#https://www.acmicpc.net/problem/13164

n, team = list(map(int,input().split()))
heights = list(map(int,input().split()))
gap = list()
# 1 3 15 26 30 35
#  2 12 11 4  5

for i in range(1,n):
    gap.append(heights[i] - heights[i-1])

gap = sorted(gap)
# print(gap)
gap = gap[:n-team]
# print(gap)
print(sum(gap))