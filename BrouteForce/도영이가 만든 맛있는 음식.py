#0704 도영이가 만든 맛있는 음식https://www.acmicpc.net/problem/2961

from itertools import combinations

n = int(input())
li = list()
for i in range(n):
    li.append(list(map(int, input().split())))
[1,2,3,4]
s= [j for j in range(n)]
sub = 999999999
for i in range(1,n+1):
    choice = list(combinations(s,i))
    for k in choice:
        sin_taste = 1
        ssum_taste = 0
        for m in k:
            sin_taste *= li[m][0]
            ssum_taste += li[m][1]
        # print(sin_taste,'sin_taste',ssum_taste,'ssum_taste')
        if sub > abs(sin_taste-ssum_taste):
            sub = abs(sin_taste-ssum_taste)
print(sub)

    