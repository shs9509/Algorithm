from itertools import product

N,M = map(int,input().split())
s= sorted(list(map(int,input().split())))

######################################
###############banila#################

# def pro(pos,S):
#     if pos == M:
#         for j in S:
#             print(j,end=' ')
#         print('')
#         return
#     else:
#         for i in range(len(s)):
#             S.append(s[i])
#             pro(pos+1,S)
#             S.pop()

# pro(0,[])

####################################
########### itertools ##############

# S = list(product(s,repeat=M))
# for j in S:
#     for k in j:
#         print(k,end=' ')
#     print('')
