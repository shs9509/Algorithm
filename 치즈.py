'''
0일때 사방탐색 하면되는거 아닌가? 안되네..

네방향에서 체크? 안되네..

뭔가 0인걸로 dfs 조지면 되지않을까... 그러면 안에있는 빈공간도 처리가된다.

0인걸 찾아서 c로 만들고 c개수 체크, c인걸 한꺼번에 0으로 처리하면서 +1


'''
cheese_pan = list()	# 치즈 판
row, col = list(map(int, input().split())) # 가로수, 세로수
for r in range(row):
    cheese_pan.append(list(map(int, input().split())))

dr = [0,0,1,-1] 
dc = [-1,1,0,0]
count = 0 # 시간 세는 변수
S = list()


setting = 1 # while문을 돌리기위해 1을 설정, 치즈의 존재유무를 확인한다.

while setting: # 치즈가 있는동안
    S.append((0,0))
    setting = 0
    count_cheese = 0
    visit = [[1] * col for _ in range(row)] #방문 안한상태 '1'
    count += 1	# while문 한바퀴 돌때마다 +1
    visit[0][0] = 0  
    while S:	# DFS
        x,y = S.pop() 
        for i in range(4): # 사방탐색
            X = x+dr[i]
            Y = y+dc[i]
            if 0<= X < row and 0<= Y < col and cheese_pan[X][Y]==1 and visit[X][Y]:
                cheese_pan[X][Y] = 0 #치즈를 만나면 0으로 만들고
                visit[X][Y] = 0		#방문 처리를 한다.
                count_cheese += 1	#치즈를 찾으면 치즈개수를 누적시킨다.
            elif 0<= X < row and 0<= Y < col and cheese_pan[X][Y]==0 and visit[X][Y]:
                visit[X][Y] = 0	#치즈가 아니면 방문처리를 하고
                S.append((X,Y))	#스택에넣어서 계속 탐색할수있도록 한다.
    for r in cheese_pan:	#치즈가 남아있는지 확인
        if 1 in r:
            setting = 1	#있으면 while문을 계속 돌린다.
            
print(count)
print(count_cheese)