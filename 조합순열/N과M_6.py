from itertools import combinations

N,M = map(int,input().split())
s= sorted(list(map(int,input().split())))

######################################
###############banila#################

def comb(start,pos,S):
    if pos == M:
        for j in S:
            print(j,end=' ')
        print('')
        return
    else:
        for i in range(start,len(s)):
            if s[i] in S:
                continue
            else:
                S.append(s[i])
                comb(i+1,pos+1,S)
                S.pop()

comb(0,0,[])

####################################
########### itertools ##############

# S = list(combinations(s,M))
# for j in S:
#     for k in j:
#         print(k,end=' ')
#     print('')