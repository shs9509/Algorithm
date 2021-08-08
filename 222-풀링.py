#https://www.acmicpc.net/problem/17829

# import copy

# scale = int(input())
# lis =list()
# for i in range(scale):
#     lis.append(list(map(int,input().split())))


# dr=[0,1,1,0]
# dc=[0,0,1,1]


# def choose_scond(L):
#     cs = sorted(L)
#     return cs[2]

# def choose_one(li,S):
#     if S ==1:
#         print(li[0][0])
#         return

#     li_after = copy.deepcopy(li)
#     for x in range(0,S,2): ## 0 2 4 6
#         for y in range(0,S,2):
#             select = list()
#             for j in range(4):
#                 X = x+dr[j]
#                 Y = y+dc[j]
#                 select.append(li[X][Y])
#             li_after[X//2][Y//2] =  choose_scond(select)
#     choose_one(li_after,S//2)

# choose_one(lis,scale)

##################################################################
# import copy

# scale = int(input())
# lis =list()
# for i in range(scale):
#     lis.append(list(map(int,input().split())))


# dr=[0,1,1,0]
# dc=[0,0,1,1]


# def choose_scond(L):
#     cs = sorted(L)
#     return cs[2]

# def choose_one(li,S):
#     if S ==1:
#         print(li[0][0])
#         return
#     for x in range(0,S,2): ## 0 2 4 6
#         for y in range(0,S,2):
#             select = list()
#             for j in range(4):
#                 X = x+dr[j]
#                 Y = y+dc[j]
#                 select.append(li[X][Y])
#             li[X//2][Y//2] =  choose_scond(select)
#     choose_one(li[0:S//2][0:S//2],S//2)

# choose_one(lis,scale)

##############################################################
import copy

scale = int(input())
lis =list()
for i in range(scale):
    lis.append(list(map(int,input().split())))


dr=[0,1,1,0]
dc=[0,0,1,1]


def choose_one(li,S):
    if S ==1:
        print(li[0][0])
        return
    for x in range(0,S,2): ## 0 2 4 6
        for y in range(0,S,2):
            select = list()
            for j in range(4):
                X = x+dr[j]
                Y = y+dc[j]
                select.append(li[X][Y])
            select.sort()
            li[X//2][Y//2] = select[2]
    choose_one(li[0:S//2][0:S//2],S//2)

choose_one(lis,scale)