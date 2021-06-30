# N, M = list(map(int, input().split()))
# P = list()
# for i in range(1,N+1):
#     P.append(str(i))

# order = []
# used =[False] * len(P)
# cnt = 1

# def perm(k,n):
#     if k == n:
#         print(' '.join(order))
#         return
#     for i in range(len(P)):
#         # if used[i]: continue  # 중복을 걸러주는 범인
#         # used[i] = True
#         order.append(P[i])

#         perm(k+1,n)

#         # used[i]= False
#         order.pop()

# perm(0,M)

####################################
########### itertools ##############

# from itertools import product

# n, m  = map(int, input().split())
# s = list()
# for i in range(1,n+1):
#     s.append(i)

# S = list(product(s,repeat=m))
# for j in S:
#     for k in j:
#         print(k,end=' ')
#     print('')

##################################
########### banila ###############

n, m  = map(int, input().split())
s = list()
for i in range(1,n+1):
    s.append(i)
#[1,2,3]

def pro(pos,S):
    if pos == m:
        print(S)
        return
    else:
        for j in s:
            S.append(j)
            pro(pos+1,S)
            S.pop()

pro(0,[])
