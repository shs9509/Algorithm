# #0624 집합의 표현 : https://www.acmicpc.net/problem/1717

# n, cal = map(int, input().split())
# cal_li = list()
# li = [[_]for _ in range(n+1)]
# for i in range(cal):
#     cal_li.append(list(map(int,input().split())))
# # print(li)

# # print(cal_li)
# for CAL in cal_li:
#     if CAL[0] == 0:
#         s = list()
#         k = list()
#         for j in range(n):
#             if CAL[1] in li[j]:
#                 s.append(j)
#             if CAL[2] in li[j]:
#                 k.append(j)
#         for S in s:
#             li[S].append(CAL[2])
#         for K in k:
#             li[K].append(CAL[1])   
#     else:
#         # print(CAL)
#         for l in li:
#             if CAL[1] in l:
#                 if CAL[2] in l:
#                     print('YES')
#                     break
#                 else:
#                     print('NO')
#                     break

############################################################

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
print(parent)
def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
        
    else:
        union(a, b)
    print(parent)

############################################

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for i in range(n + 1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    elif opr == 1:
        if find_parent(a) == find_parent(b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")