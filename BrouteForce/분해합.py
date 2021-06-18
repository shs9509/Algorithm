#https://www.acmicpc.net/problem/2231
n = int(input())
li= list()

for i in range(n):
    N = n-i
    val=0
    while N!=0:
        val += N%10
        N = N//10
    if val == i :
        li.append(val)
if li:
    print(n-li[-1])
else:
    print(0)

## 이건 0부터 계산하잖아
## 근데 4자리수면 9999 36을 빼고 거기부터 시작하면됨