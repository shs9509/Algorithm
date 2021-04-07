def dfs():
    S =[(1,1)]
    visit = [[False for _ in range(100)] for _ in range(100)]
    visit[1][1] = True
    while S:
        x,y = S.pop()
        for j in range(4):
            nx = x+dr[j]
            ny = y+dc[j]
            if visit[nx][ny] == False and 0<nx<100 and 0<ny<100:
                if miro[nx][ny] == 3:
                    return 1
                if miro[nx][ny] == 0:
                    visit[nx][ny]= True
                    S.append((nx,ny))
    return 0
for num in range(10):
    tc = int(input())
    miro = list()
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    for i in range(100):
        miro.append(list(map(int, input())))

    # print(miro)
    print("#{} {}".format(tc,dfs()))