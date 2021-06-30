# from itertools import permutations

# N,M = map(int,input().split())
# s= sorted((list(map(int,input().split()))))
# visit= [False for _ in range(len(s))]
# ######################################
# ###############banila#################

# def per(pos,S,v):
#     P = 0
#     if pos == M:
#         print(' '.join(map(str, S)))
#         return
#     else:
#         for i in range(len(s)):
#             if v[i] == False and P !=s[i]:
#                 v[i] = True
#                 P = s[i]
#                 S.append(s[i])
#                 per(pos+1,S,v)
#                 S.pop()
#                 v[i] = False

# per(0,[],visit)

####################################
########### itertools ##############

import sys
from itertools import permutations


n, m = map(int, input().split())
arr = input().split()
arr.sort(key=lambda x:int(x))
answer = []
visited = set()

for p in permutations(arr, m):
    s = ' '.join(p)
    if s not in visited:
        answer.append(s)
        visited.add(s)
    
[print(c) for c in answer]
