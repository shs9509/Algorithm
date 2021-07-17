#0718 가장 큰 증가 부분 수열 https://www.acmicpc.net/problem/11055
import copy
n = int(input())
li = list(map(int,input().split()))
tmp = copy.deepcopy(li)
#  1 100 2 50 60 3 5 6 7 8
#  1 101 3 53 113 6
for i in range(0,n):
    for j in range(i,-1,-1):
        # print(i,j)
        if li[i]> li[j]:
            if tmp[i] < li[i] + tmp[j]:
                tmp[i] = li[i] + tmp[j]

# print(tmp)
print(max(tmp))