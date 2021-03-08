def perm(start,n,k,li):
    if n == k:
        print(' '.join(map(str,order)))
        return
    for i in range(start,li[0]):
        if visit[i] == True:
            continue
        else:
            visit[i] = True
            order.append(li[i+1])
            perm(i+1,n+1,k,li)
            visit[i] = False
            order.pop()

while True:
    order = []
    lotto = list(map(int, input().split()))
    visit = [False] * lotto[0]
    if 0 in lotto:
        break
    else:
        perm(0,0,6,lotto)
        print('')