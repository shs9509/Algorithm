# https://www.acmicpc.net/problem/1806

num, obj = map(int,input().split())
li = list(map(int,input().split()))
s=0
e=1
sum_val = li[s]
min_length =1000000
while(s<=e):
    if sum_val>=obj:
        min_length = min(e-s,min_length)
        sum_val-=li[s]
        s+=1
        # print(sum(li[s:e]))
        if s>=num:
            break
    else:
        if e>=num:
            break
        else:
            sum_val+=li[e]
            e+=1

    # print(s,e,sum_val)
if min_length == 1000000:
    print('0')
else:
    print(min_length)

