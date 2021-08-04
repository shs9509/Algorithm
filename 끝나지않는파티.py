#https://www.acmicpc.net/problem/11265

n, times = list(map(int,input().split()))
li= list()
for i in range(n):
    li.append(list(map(int,input().split())))

def floid(lis):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                lis[j][k] = min(lis[j][k], lis[j][i]+lis[i][k] )

floid(li)
for time in range(times):
    start, end, t = list(map(int,input().split()))
    if li[start-1][end-1]<=t:
        print('Enjoy other party')
    else:
        print('Stay here')


# def find_route(S,E,T,V,C):
#     if V>T:
#         return
#     if S==E:
#         if T>=V:
#             possible = True
#         return
#     else:
#         for j in range(n):
#             if C[j]:
#                 continue
#             else:
#                 C[j] = True
#                 find_route(j,E,T,V+li[S][j],C)
#                 C[j] = False
#         else:
#             return


# for time in range(times):
#     check = [False for _ in range(n)]
#     start, end, t = list(map(int,input().split()))
#     possible = False
#     if li[start-1][end-1] <= t:
#         print('Enjoy other party')
#         continue
#     else:
#         check[start-1] = True
#         find_route(start-1,end-1,t,0,check)

#     if possible:
#         print('Enjoy other party')
#     else:
#         print('Stay here')
