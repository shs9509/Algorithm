#https://www.acmicpc.net/problem/15787

N, M = map(int, input().split()) #기차수, 명령수

train = [[0 for _ in range(20)] for _ in range(N)]

for i in range(M):
    li = list()
    li = list(map(int,input().split()))
    if len(li)==3:
        order, train_num, seat_num = li
    else:
        order, train_num = li
    # print(li)
    if order==1:
        train[train_num-1][seat_num-1] = 1
    elif order ==2:
        train[train_num-1][seat_num-1] = 0
    elif order ==3:
        for j in range(19,0,-1):
            # print(j)
            train[train_num-1][j] = train[train_num-1][j-1]
        train[train_num-1][0] = 0
    else:
        for k in range(1,19):
            train[train_num-1][k-1] = train[train_num-1][k]
        train[train_num-1][19] = 0
# print(train)
result = set()
for k in train:
    result.add(str(k))
print(len(result))