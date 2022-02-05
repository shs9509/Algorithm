# https://www.acmicpc.net/problem/22945
N = int(input())
li = list(map(int,input().split()))
s = 0
e = N-1
max_val =0
while(s<e):
    min_val = min(li[s],li[e])
    max_val= max(max_val,(e-s-1)*min_val)
    if min_val==li[s]:
        s+=1
    else:
        e-=1
print(max_val)