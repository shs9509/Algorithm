#https://www.acmicpc.net/problem/15661
'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
import copy
from itertools import combinations, count
n = int(input())
idx = [ k for k in range(1,n+1)]
li= list()
sum_val = 0
min_val = 999999999999
flag = False
for i in range(n):
    li.append(list(map(int,input().split())))

for l in li:
    sum_val+=sum(l)

for j in range(1,n//2+1):
    comb_li = combinations(idx,j) #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    for comb in comb_li:    # (1, 2)
        count_a = 0
        count_b = 0
        for x in comb: # 1,2
            for y in comb: # 1,2
                count_a += li[x-1][y-1] # 1,1 1,2 2,1 2,2
        remain = list(set(idx) -set(comb))
        for a in remain:
            for b in remain:
                count_b+= li[a-1][b-1]
        # print(comb,remain)
        # print(abs(count_b-count_a))
        if min_val>abs(count_b-count_a):
            min_val = abs(count_b-count_a)
        if min_val == 0:
            flag = True
            break
    if flag:
        break
                
print(min_val)

