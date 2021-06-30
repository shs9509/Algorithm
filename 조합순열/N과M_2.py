#https://www.acmicpc.net/problem/15650
# n, m = map(int, input().split())  # 3 1 # 123 에서 부분집합 길이 1

# arr = [1 + i for i in range(n)]   # 숫자 리스트     [1,2,3]
# used = [False] * n                # 중복숫자 체크   [false false false]
# order = []                                # 출력할 수열
# def perm(start,k):
#     if k == m:
#         print(*order)
#         return
#     for i in range(start,n):
#         if used[i]: continue
#         used[i] = True
#         order.append(arr[i])
#         perm(i+1,k + 1)
#         used[i] = False
#         order.pop()


# perm(0,0)

####################################
########### itertools ##############

# from itertools import combinations

# n, m  = map(int, input().split())
# s = list()
# for i in range(1,n+1):
#     s.append(i)

# S = list(combinations(s,m))
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

def comb(start,pos,S):
    if pos == m:
        print(S)
        return
    else:
        for j in range(start,len(s)):
            if s[j] in S:
                continue
            else:
                S.append(s[j])
                comb(j,pos+1,S)
                S.pop()
comb(0,0,[])
