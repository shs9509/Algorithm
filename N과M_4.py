N, M = list(map(int, input().split()))
P = list()
for i in range(1,N+1):
    P.append(str(i))

order = []
used =[False] * len(P)
cnt = 1

def perm(start, k, n):
    if k == n:
        print(' '.join(order))
        return
    for i in range(start, len(P)):
        # if used[i]: continue
        used[i] = True
        order.append(P[i])

        perm(i, k+1, n)

        used[i]= False
        order.pop()

perm(0,0,M)
