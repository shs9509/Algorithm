# #https://www.acmicpc.net/problem/15686
# # 0:빈칸 1:집 2:치킨집
# # 각각의 집은 치킨거리를 갖고있고 이거의 합이 도시의 치킨거리 이게 가장 작아야됨
# # 치킨집의 최대 개수 M개를 택해서
# # 그러면 M개를 택해서 치킨거리 구하기

# def find_chicken_length(lis):# 고른치킨점에서 치킨거리 구하기
#     ans_length = 0
#     for h in home:
#         length=10000000000
#         home_x, home_y = h
#         for l in lis:
#             chicken_x, chicken_y = l
#             if abs(home_x-chicken_x)+abs(home_y-chicken_y)<=length:
#                 length = abs(home_x-chicken_x)+abs(home_y-chicken_y)
#         ans_length += length
#     return ans_length

# def select(start,lis,num): # 치킨 위치중에서 num개의 위치고르기
#     if len(lis)==num:
#         length_li.append(find_chicken_length(lis))
#         return
#     else:
#         for i in range(start,len(chicken)):
#             if len(S)+len(chicken)-i<num:
#                 break
#             else:
#                 S.append(chicken[i])
#                 select(i,S,num)
#                 S.pop()

# scale, need_num = map(int, input().split())
# li = list() # 주어진 리스트
# chicken = list() # 치킨집 좌표리스트
# home = list() # 집 좌표리스트
# length_li = list()
# for i in range(scale):
#     li.append(list(map(int,input().split())))

# for x in range(scale):
#     for y in range(scale):
#         if li[x][y]==2:
#             chicken.append([x,y])
#         elif li[x][y]==1:
#             home.append([x,y])
# S = list()
# select(0,S,need_num)
# print(min(length_li))

## 시간 초과 걸리 메모이제이션 써야되겟는데


def find_chicken_length(lis):# 고른치킨점에서 치킨거리 구하기
    for h in range(len(home)):
        length=10000000000
        home_x, home_y = home[h]
        for l in lis:
            chicken_x, chicken_y = l
            home_length[h].append(abs(home_x-chicken_x)+abs(home_y-chicken_y))
    return

def select(start,lis,num): # 치킨 위치중에서 num개의 위치고르기
    if len(lis)==num:
        min_length=0
        for hom in home_length:
            length =1000000000
            for l in lis:
                if hom[l]< length:
                    length = hom[l]
            min_length += length
        length_li.append(min_length)
        return
    else:
        for i in range(start,len(chicken)):
            if len(S)+len(chicken)-i<num:
                break
            else:
                S.append(i)
                select(i,S,num)
                S.pop()


scale, need_num = map(int, input().split())
li = list() # 주어진 리스트
chicken = list() # 치킨집 좌표리스트
chicken_length_li = list()
home = list() # 집 좌표리스트
length_li = list()
for i in range(scale):
    li.append(list(map(int,input().split())))

for x in range(scale):
    for y in range(scale):
        if li[x][y]==2:
            chicken.append([x,y])
        elif li[x][y]==1:
            home.append([x,y])
S = list()
home_length =[[]for _ in range(len(home))] # 집에서 치킨집마다의 거리
find_chicken_length(chicken)
select(0,S,need_num)
print(min(length_li))