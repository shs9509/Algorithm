scale = int(input())
zido = list()
dr = [1,0,0,-1]   #[1,1,1,0,0,-1,-1,-1] 상하좌우만!
dc = [0,1,-1,0]
count_house= list()
for i in range(scale):
    zido.append(list(map(int,input())))
# print(zido)
count = 1
while True:
    capture = True
    count_one = 0
    for x in range(scale):
        for y in range(scale):
            if zido[x][y] == 1:
                start_x = x
                start_y = y
                capture = False
                count_one += 1
                break
        if capture == False: # 1만나면 잠깐 벗어나기
            break
    if count_one == 0:  # 1인거 없으면 이곳을 뜨자
        break
    count +=1   # count는 집의 인덱스를 나타냄
    S = list()
    S.append([start_x,start_y])
    house = 0   # 집의 개수
    while len(S) != 0:
        start_x,start_y = S.pop()
        zido[start_x][start_y] = count
        house +=1
        for i in range(4):
            X = start_x + dr[i]
            Y = start_y + dc[i]
            if 0 <= X < scale and 0 <= Y < scale:
                if zido[X][Y] == 1 and not [X,Y] in S:
                    S.append([X,Y])
    count_house.append(house)   # 각집이 몇개있는지 알려줌

print(count-1)
count_house.sort()
for house_num in count_house:
    print(house_num)
