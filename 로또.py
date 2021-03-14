#https://www.acmicpc.net/problem/6603

def perm(start,n,k,li):
    if n == k:
        print(' '.join(map(str,order))) # 출력
        return
    for i in range(start,li[0]): # 중복을 없애기 위해서 start부터 시작한다.
        if visit[i] == True:
            continue
        else:
            visit[i] = True
            order.append(li[i+1])
            perm(i+1,n+1,k,li)
            visit[i] = False
            order.pop()

while True:
    order = []	# 출력되는 로또
    lotto = list(map(int, input().split())) # 주어진 로또 후보군
    visit = [False] * lotto[0] # 출력된 로또 확인
    if 0 in lotto:	# input에서 0 있으면 while문을 빠져나온다.
        break
    else:
        perm(0,0,6,lotto)
        print('')