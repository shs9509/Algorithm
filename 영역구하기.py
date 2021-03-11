dr = [1,0,0,-1]
dc = [0,1,-1,0]
count = 0 
square = list()
row, col, num = list(map(int, input().split())) # 가로줄, 세로줄, 영역 # 5,7,3
paper = [[1 for _ in range(col)] for a in range(row)] # 1으로 이루어진 모눈 종이

for i in range(num):
    a,b,c,d = list(map(int, input().split())) # [0,2] [4,4]
    for R in range(a,c): # 가로를 0에서 4만큼
        for C in range(b,d): # 세로를 2에서 4만큼
            paper[C][R] = 0     #모눈종이에 0로 체크를한다

for x in range(row):
    for y in range(col):
        if paper[x][y]:   # 원하는색깔이며 방문하지 않았다!
            start_x = x
            start_y = y # x,y 그대로쓰면 밑에서 위의 for문의 xy가 바뀜
            
            S = list()
            S.append([start_x,start_y])
            check = 1
            while S:
                start_x, start_y = S.pop()
                for i in range(4):
                    X = start_x + dr[i]
                    Y = start_y + dc[i]
                    if 0 <= X < row and 0 <= Y < col:
                        if paper[X][Y]:
                            paper[X][Y] = 0 # 방문 체크해주기
                            S.append([X,Y])
                            check +=1
            square.append(check) # 1일경우 어떻하지?????

square.sort()
print(count)
print(' '.join(map(str,square)))
