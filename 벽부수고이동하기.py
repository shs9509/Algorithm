#https://www.acmicpc.net/problem/2206

'''
1을 통과할떄 flag 같은거 정하면 한번은 봐주지않을까
if == 1 and flag =True 
이런식으로

'''
# dr=[-1,1,0,0]
# dc=[0,0,1,-1]

# row, col = list(map(int, input().split()))
# road = list()
# for r in range(row):
#     road.append(list(map(int,input())))

# # print(row, col, road)

# def bfs():
#     S= list()
#     S.append((0,0,True,1))
#     visit= [[0 for a in range(col)] for _ in range(row)]
#     # print(visit)
#     visit[0][0]= 1
#     while S:
#         x,y,flag,length = S.pop(0)
#         L = length
#         for i in range(4):
#             # print(S)
#             X = x+dr[i]
#             Y = y+dc[i]
#             if 0 <= X < row and 0 <= Y <col:
#                 if road[X][Y] == 0 and visit[X][Y] ==0:
#                     visit[X][Y] =1
#                     S.append((X,Y,flag,length+1))
#                 elif road[X][Y] == 1 and visit[X][Y] ==0:
#                     if flag:
#                         visit[X][Y] =1
#                         S.append((X,Y,False,length+1))
                    
#     print(visit)
    
#     if visit[row-1][col-1]==0:
#         return -1
#     else:
#         return L

# print(bfs())



# import sys
# from collections import deque
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs():
#     q = deque()
#     q.append([0, 0, 1])
#     visit = [[[0] * 2 for i in range(m)] for i in range(n)]
#     visit[0][0][1] = 1
#     while q:
#         a, b, w = q.popleft()
#         if a == n - 1 and b == m - 1:
#             return visit[a][b][w]
#         for i in range(4):
#             x = a + dx[i]
#             y = b + dy[i]
#             if 0 <= x < n and 0 <= y < m:
#                 if s[x][y] == 1 and w == 1:
#                     visit[x][y][0] = visit[a][b][1] + 1
#                     q.append([x, y, 0])
#                 elif s[x][y] == 0 and visit[x][y][w] == 0:
#                     visit[x][y][w] = visit[a][b][w] + 1
#                     q.append([x, y, w])
#         print(visit)
#     return -1
# n, m = map(int, input().split())
# s = []
# for i in range(n):
#     s.append(list(map(int, list(input().strip()))))
# print(bfs())

dr=[-1,1,0,0]
dc=[0,0,1,-1]

row, col = list(map(int, input().split()))
road = list()
for r in range(row):
    road.append(list(map(int,input())))

# print(row, col, road)

def bfs():
    S= list()
    S.append((0,0,True))
    visit= [[0 for a in range(col)] for _ in range(row)]
    # print(visit)
    visit[0][0]= 1
    while S:
        x,y,flag = S.pop(0)
        for i in range(4):
            print(S)
            X = x+dr[i]
            Y = y+dc[i]
            if 0 <= X < row and 0 <= Y <col:
                if visit[X][Y] == 0:
                    if road[X][Y] == 0 :
                        S.append((X,Y,flag))
                        visit[X][Y] = visit[x][y] + 1

                    elif road[X][Y] == 1 and flag:
                        S.append((X,Y,False))
                        visit[X][Y] = visit[x][y] + 1
                elif visit[X][Y] == visit[x][y]+1 and (X,Y,False) in S and flag:
                    S.append((X,Y,True))
    print(visit)
    
    if visit[row-1][col-1]==0:
        return -1
    else:
        return visit[row-1][col-1]

print(bfs())

'''
6 4
0000
2140
0000
0000
0111
0000

[1, 2, 3, 4], 
[2, 3, 4, 5], 
[3, 4, 5, 6],
[4, 5, 6, 7],
[5, 0, 0, 8],
[6, 7, 8, 9],


'''