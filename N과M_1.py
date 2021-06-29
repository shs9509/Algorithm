#https://www.acmicpc.net/problem/15649
# n, m = map(int, input().split())  # 3 1 # 123 에서 부분집합 길이 1

# arr = [1 + i for i in range(n)]   # 숫자 리스트     [1,2,3]
# used = [False] * n                # 중복숫자 체크   [false false false]
# order = []                                # 출력할 수열

# def perm(k):
#     if k == m:
#         print(*order)
#         return
#     for i in range(n):
#         if used[i]: continue
#         used[i] = True
#         order.append(arr[i])
#         perm(k + 1)
#         used[i] = False
#         order.pop()
# perm(0)

# N, M = map(int,input().split())
# s = list()
# for i in range(1,N+1):
#     s.append(i)
# # [1,2,3]

# def per(pos,S):
#     if pos == M:
#         for k in S:
#             print(k,end=' ')
#         print('')
#         return
#     else:
#         for j in range(N):
#             if s[j] in S:
#                 continue
#             else:
#                 S.append(s[j])
#                 per(pos+1,S)
#                 S.pop()

# per(0,[])

# from itertools import permutations

# N, M = map(int,input().split())
# s = list()
# for i in range(1,N+1):
#     s.append(i)
# # [1,2,3]
# S = list(permutations(s,M))
# for j in S:
#     for k in j:
#         print(k,end=' ')
#     print('')

from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print(li)
print('\n'.join(list(map(' '.join,permutations(li, M)))))