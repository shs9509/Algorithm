#https://www.acmicpc.net/problem/20364
import copy

length,duck = map(int,input().split())
li = [0]*(length+1)
result = list()
for i in range(duck):
    pos = int(input())#3
    pre_pos = copy.copy(pos)#3
    before_pos = pos # 3
    check = 0
    while before_pos!=0:
        if li[before_pos]==1:
            check = before_pos
        before_pos = pos // 2
        pos = before_pos 
    if check:
        result.append(check)
    else:
        li[pre_pos]=1
        result.append(check)

for j in result:
    print(j)

