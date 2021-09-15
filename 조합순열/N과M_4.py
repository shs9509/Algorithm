# N, M = list(map(int, input().split()))
# P = list()
# for i in range(1,N+1):
#     P.append(str(i))

# order = []
# used =[False] * len(P)
# cnt = 1

# def perm(start, k, n):
#     if k == n:
#         print(' '.join(order))
#         return
#     for i in range(start, len(P)):
#         # if used[i]: continue
#         used[i] = True
#         order.append(P[i])

#         perm(i, k+1, n)

#         used[i]= False
#         order.pop()

# perm(0,0,M)

####################################
########### itertools ##############

from itertools import combinations_with_replacement

n, m  = map(int, input().split())
s = list()
for i in range(1,n+1):
    s.append(i)
#[1,2,3]

S =list(combinations_with_replacement(s,m))
for j in S:
    for k in j:
        print(k,end=' ')
    print('')




##################################
########### banila ###############

n, m  = map(int, input().split())
s = list()
for i in range(1,n+1):
    s.append(i)
#[1,2,3]

def increase_pro(start,pos,S):
    if pos == m:
        print(S)
        return
    else:
        for j in range(start,len(s)):
            S.append(s[j])
            increase_pro(j,pos+1,S)
            S.pop()

increase_pro(0,0,[])
