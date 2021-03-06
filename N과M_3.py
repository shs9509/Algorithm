N, M = list(map(int, input().split()))
P = list()
for i in range(1,N+1):
    P.append(str(i))

order = []
used =[False] * len(P)
cnt = 1

def perm(k,n):
    if k == n:
        print(' '.join(order))
        return
    for i in range(len(P)):
        # if used[i]: continue  # 중복을 걸러주는 범인
        # used[i] = True
        order.append(P[i])

        perm(k+1,n)

        # used[i]= False
        order.pop()

perm(0,M)
