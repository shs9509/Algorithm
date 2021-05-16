#https://www.acmicpc.net/problem/17144

def munzi(first_lis,lis,now,second):
    next_li= [[0 for in range(row)] for in range(col)]
    for X in range(len(lis)):
        for Y in range(len(lis[0])):
            if lis[X][Y] != -1 and lis[X][Y] != 0:
                val = lis[X][Y]
                for j in range(4):
                    d_X = X+dr[j]
                    d_Y = Y+dc[j]
                    if 0<=d_X <row and 0<d_Y<=col and [d_X,d_Y] not in air_cleaner:
                        first_lis[d_X][d_Y] = val//5
                        lis[X][Y] -= val//5
            
    a1_x = air_cleaner[0][0] 
    a1_y = air_cleaner[0][1] 
    a2_x = air_cleaner[1][0] 
    a2_y = air_cleaner[1][1] 
    
    lis[a1_x-1][a1_y]= 0 
    lis[a1_x-1][a1_y]= 0 
    

dr =[1,-1,0,0]
dc =[0,0,-1,1]
row, col, sec = map(int,input().split())
li = list()
for i in range(row):
    li.append(list(map(int,input().split())))

air_cleaner = list()
first_li= [[0 for in range(row)] for in range(col)]

for x in range(row):
    for y in range(col):
        if li[x][y]==-1:
            air_cleaner.append([x,y])

munzi(first_li,li,0,sec)





# ///////////////////////////////////////////////#
# 공기청정기 위치 파악
def air_position():
    for i in range(R):
        if arr[i][0] == -1:
            return [i, 0], [i + 1, 0]  # 위, 아래 공기청정기 위치


# 미세먼지 이동
def dust_move():
    temp = [[0] * C for _ in range(R)]  # 확산값 저장
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                val = 0  # 얼마나 확산했는지
                # 상
                if i - 1 >= 0 and arr[i - 1][j] != -1:
                    temp[i - 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5
                # 하
                if i + 1 < R and arr[i + 1][j] != -1:
                    temp[i + 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5
                # 좌
                if j - 1 >= 0 and arr[i][j - 1] != -1:
                    temp[i][j - 1] += arr[i][j] // 5
                    val += arr[i][j] // 5
                # 우
                if j + 1 < C and arr[i][j + 1] != -1:
                    temp[i][j + 1] += arr[i][j] // 5
                    val += arr[i][j] // 5
                temp[i][j] -= val  # 확산값 빼기
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]  # 확산받은 값 더하기


def air_move():
    # up
    # 1 - 아래
    temp = arr[up[0]][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    arr[up[0]][1] = 0

    # 2 - 오른쪽
    temp_1 = arr[0][C - 1]
    for i in range(up[0] - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up[0] - 1][C - 1] = temp

    # 3 - 위쪽
    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(up[0] - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    # down
    # 1- 위쪽
    temp = arr[down[0]][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down[0]][i] = arr[down[0]][i - 1]
    arr[down[0]][1] = 0

    # 2 오른쪽
    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down[0] + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down[0] + 1][C - 1] = temp

    # 3 - 아래쪽
    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(down[0] + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2


if __name__ == "__main__":

    # input
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    # 공기청정기 위치 가져오기
    up, down = air_position()

    # T시간 동안 시뮬레이션
    for i in range(T):
        dust_move()  # 미세먼지 이동
        air_move()  # 공기청정기 작동


    total = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                total += arr[i][j]
    print(total)