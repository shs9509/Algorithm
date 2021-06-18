#https://www.acmicpc.net/problem/2798

## 1
def blackjack(l,m,sum_val,start):
    if m==3:
        p.append(sum_val)
        return
    else:
        for i in range(start,n):
            sum_val += li[i]
            if sum_val<=max_val:
                blackjack(l,m+1,sum_val,i+1)
            sum_val -= li[i]

n, max_val = map(int,input().split())
li = list(map(int, input().split()))
p=list()
s = 0
blackjack(li,0,s,0)
print(max(p))


## 2
n, max_val = map(int,input().split())
li = list(map(int, input().split()))
val =0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if val < li[i]+li[j]+li[k] <= max_val:
                val = li[i]+li[j]+li[k]
            else:
                continue
print(val)