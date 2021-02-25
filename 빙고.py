bingo_pan = list()
for i in range(5):
    bingo_pan.append(list(map(int,input().split())))
number_li = list()
for j in range(5):
    number_li.append(list(map(int,input().split())))

count = 0
number = 0
flag = True

for k in range(5):
    for m in number_li[k]:
        number +=1
        for x in range(5):
            for y in range(5):
                if bingo_pan[x][y] == m:
                    bingo_pan[x][y] = 0
        
        for x in range(5):          # 가로
            for y in range(5):
                if bingo_pan[x][y] == 0:
                    continue
                else:
                    break
            else:
                count += 1

        for x in range(5):      # 세로
            for y in range(5):
                if bingo_pan[y][x] == 0:
                    continue
                else:
                    break
            else:
                count += 1

        for x in range(5):     # 대각
            if bingo_pan[x][x] == 0:
                continue
            else:
                break
        else:
            count += 1

        for x in range(5):      # 역대각
            if bingo_pan[x][4-x] == 0:
                continue
            else:
                break
        else:
            count += 1
        
        if count >=3:
            print(number)
            flag = False
            break
        else:
            count = 0
    if flag == False:
        break