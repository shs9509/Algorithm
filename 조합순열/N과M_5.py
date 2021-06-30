from itertools import permutations
N,M = map(int,input().split())
s= sorted(list(map(int,input().split())))

######################################
###############banila#################

# def per(pos,S):
#     if pos == M:
#         for j in S:
#             print(j,end=' ')
#         print('')
#         return
#     else:
#         for i in range(len(s)):
#             if s[i] in S:
#                 continue
#             else:
#                 S.append(s[i])
#                 per(pos+1,S)
#                 S.pop()

# per(0,[])

####################################
########### itertools ##############

S = list(permutations(s,M))
for j in S:
    for k in j:
        print(k,end=' ')
    print('')
