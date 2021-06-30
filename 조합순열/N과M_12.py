from itertools import combinations_with_replacement

N,M = map(int,input().split())
s= sorted(list(map(int,input().split())))

######################################
###############banila#################

def comb_rep(start,pos,S):
    if pos == M:
        for j in S:
            print(j,end=' ')
        print('')
        return
    P=0
    for i in range(start,len(s)):
        if P !=s[i]:
            P=s[i]
            S.append(s[i])
            comb_rep(i,pos+1,S)
            S.pop()

comb_rep(0,0,[])

####################################
########### itertools ##############

# N,M = map(int,input().split())
# s= sorted(list(set(list(map(int,input().split())))))

# S = list(combinations_with_replacement(s,M))
# for j in S:
#     for k in j:
#         print(k,end=' ')
#     print('')
