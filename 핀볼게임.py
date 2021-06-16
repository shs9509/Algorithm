def start(li,x,y,dir):
    x= x+dr[dir]
    y= y+dc[dir]
    if 0>x or x>=scale or y<0 or y>=scale:
        return False 
    elif x ==0 and dir==3:
        return False
    elif x==scale-1 and dir==2:
        return False
    elif y==0 and dir==1:
        return False
    elif y==scale-1 and dir ==0:
        return False
    elif li[x][y] == -1:
        return False
    elif dir==0 and (li[x][y] in [1,2,5]):
        return False
    elif dir ==1 and (li[x][y] in [3,4,5]):
        return False
    elif dir ==2 and (li[x][y] in [2,3,5]):
        return False
    elif dir ==3 and (li[x][y] in [1,4,5]):
        return False
    else: 
        return True
  
def pinball(lis,points):
    score = list()
    while(points):
        x,y=points.pop()
        start_x = x
        start_y = y
        X =x
        Y =y
        
        for direction in range(4):
            if start(lis,X,Y,direction):
                print(X,Y,direction)
                count = 0
                while(True):
                    # print('지금은',(X,Y),'방향은',direction)
                    X = X+dr[direction]
                    Y = Y+dc[direction]
                    # print('지금은',(X,Y),'방향은',direction)
                    if X==start_x and Y ==start_y: # 시작지점
                        score.append(count)
                        break
                    elif li[X][Y]==-1: #블랙홀
                        score.append(count)
                        break
                    elif li[X][Y]==0 and X==0 and direction==3: # 북쪽벽 만남
                        count +=1
                        direction=2
                    elif li[X][Y]==0 and X==scale-1 and direction ==2: # 남쪽벽 만남
                        count +=1
                        direction=3
                    elif li[X][Y]==0 and Y==0 and direction==1: # 서쪽벽 만남
                        count+=1
                        direction = 0
                    elif li[X][Y]==0 and Y==scale-1 and direction==0: # 동쪽벽 만남
                        count+=1
                        direction =1
                    elif 6<=li[X][Y]<=10:
                        X, Y = wormwhole_li[X][Y]
                    elif 1<=li[X][Y]<=5:
                        if li[X][Y]==5:
                            if direction==0:
                                direction=1
                            elif direction==1:
                                direction=0
                            elif direction==2:
                                direction=3
                            else:
                                direction=2
                        elif li[X][Y]==1:
                            if direction==0:
                                direction=1
                            elif direction==1:
                                direction=3
                            elif direction==2:
                                direction=0
                            else:
                                direction=2
                        elif li[X][Y]==2:
                            if direction==0:
                                direction=1
                            elif direction==1:
                                direction=2
                            elif direction==2:
                                direction=3
                            else:
                                direction=0
                        elif li[X][Y]==3:
                            if direction==0:
                                direction=2
                            elif direction==1:
                                direction=0
                            elif direction==2:
                                direction=3
                            else:
                                direction=1
                        else:
                            if direction==0:
                                direction=3
                            elif direction==1:
                                direction=0
                            elif direction==2:
                                direction=1
                            else:
                                direction=2
                        count +=1
                    print('새로운방향은',direction)
                print(score)
    return score

tc = int(input())
dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 0동 1서 2남 3북
for tc_num in range(tc):
    scale = int(input())#크기
    li = list()#핀볼배치
    wormwhole = [0,0,0,0,0,(1,2),0,0,0,0,0]
    wormwhole_li = [[0 for _ in range(scale)] for _ in range(scale)]
    blackwhole = list()
    for i in range(scale):
        li.append(list(map(int,input().split())))
    start_point_li =list()
    for x in range(scale):
        for y in range(scale):
            if li[x][y]==0:
                start_point_li.append((x,y))
            elif 6<=li[x][y]<10:
                if wormwhole[li[x][y]]:
                    wormwhole_x, wormwhole_y = wormwhole[li[x][y]]
                    wormwhole_li[x][y] = (wormwhole_x,wormwhole_y)
                    wormwhole_li[wormwhole_x][wormwhole_y] = (x,y)
                else:
                    wormwhole[li[x][y]]=(x,y)
            elif li[x][y]==-1:
                blackwhole.append((x,y))
    print(pinball(li,start_point_li))


    
####################################################################
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 1~5 블럭 방향전환
change = (
    'dummy',
    (1, 3, 0, 2),
    (3, 0, 1, 2),
    (2, 0, 3, 1),
    (1, 2, 3, 0),
    (1, 0, 3, 2)
)


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input()) + 2
    # 가장자리에 5번 블럭 더함
    MAP = [[5] * N] + [[5] + list(map(int, input().split())) + [5] for _ in range(N - 2)] + [[5] * N]

    # 웜홀
    worm_stack = ['dummy'] * 6 + [None] * 5
    wormhole = {}
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if MAP[r][c] in range(6, 11):
                # MAP[r][c]=6
                worm_start = worm_stack[MAP[r][c]] # worm_stack[6] = None > worm_stack[6]=(1,2) > worm_start 
                if not worm_start:
                    worm_stack[MAP[r][c]] = (r, c) # worm_stack[6] =(1,2)
                else:
                    wormhole[worm_start] = (r, c)  # 딕셔너리로 서로저장
                    wormhole[(r, c)] = worm_start

    # 탐색
    result = 0
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if MAP[r][c] == 0:
                for d in range(4):  # 상하좌우
                    cnt = 0
                    y, x = r + dy[d], c + dx[d]
                    while True:
                        # 시작지점이거나 블랙홀이면 종료
                        if (y, x) == (r, c) or MAP[y][x] == -1:
                            break

                        # 1 ~ 5 블럭에 와있으면 방향 전환, 득점
                        elif MAP[y][x] in range(1, 6):
                            d = change[MAP[y][x]][d]
                            cnt += 1

                        # 6 ~ 10 블럭에 와있으면 워프
                        elif MAP[y][x] in range(6, 11):
                            y, x = wormhole[(y, x)]

                        # 한 칸 전진
                        y, x = y + dy[d], x + dx[d]

                    # 탐색 종료되면 결과 갱신
                    if cnt > result:
                        result = cnt

    print('#{} {}'.format(test_case, result))