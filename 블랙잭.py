#https://www.acmicpc.net/problem/2798

num, sum_val = list(map(int , input().split()))
card = list(map(int , input().split()))
visit = [False] * num
order =  []
li = list()
def perm(k,n,a):
    if k == 3:
        val = sum(order)
        if val <= a :
            li.append(val)
        return
    for i in range(n):
        if visit[i]:
            continue
        else:
            visit[i] = True
            order.append(card[i])

            perm(k+1, n, a)

            visit[i] = False
            order.pop()

perm(0,num,sum_val)
print(max(li))
