from itertools import combinations

N,M = map(int,input().split())
s= sorted((list(map(int,input().split()))))
visit= [False for _ in range(len(s))]
# ######################################
# ###############banila#################

def per(start,pos,S,v):
    P = 0
    if pos == M:
        print(' '.join(map(str, S)))
        return
    else:
        for i in range(start,len(s)):
            if v[i] == False and P !=s[i]:
                v[i] = True
                P = s[i]
                S.append(s[i])
                per(i+1,pos+1,S,v)
                S.pop()
                v[i] = False

per(0,0,[],visit)

####################################
########### itertools ##############
# answer = []
# S = list(combinations(s,M))
# for j in S:
#     if j in answer:
#         continue
#     else:
#         answer.append(j)

# for k in answer:
#     print(' '.join(map(str,k)))