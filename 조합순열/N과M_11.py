# from itertools import product

# N,M = map(int,input().split())
# s= sorted(list(map(int,input().split())))


######################################
###############왜안됨#################
# P = []
# def pro(pos,S):
#     global P
#     if pos == M:
#         if S in P:
#             return #### 왜안되지
#         else:
#             P.append(S)
#             for j in S:
#                 print(j,end=' ')
#             print('')
#             return
#     else:
#         for i in range(len(s)):
#             S.append(s[i])
#             pro(pos+1,S)
#             S.pop()

# pro(0,[])

######################################
###############banila#################
# def pro(pos,S):
#     if pos == M:
#             print(' '.join(map(str,S)))
#             return
#     P = 0
#     for i in range(len(s)):
#         if P!=s[i]:
#             P=s[i]
#             S.append(s[i])
#             pro(pos+1,S)
#             S.pop()

# pro(0,[])



####################################
########### itertools ##############
# 시간초과
from itertools import product

N,M = map(int,input().split())
s= sorted(list(set(list(map(int,input().split())))))
answer =[]
S = list(product(s,repeat=M))
for j in S:
    if j in answer:
        continue
    else:
        answer.append(j)

for k in answer:
    print(' '.join(map(str,k)))