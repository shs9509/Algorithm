O_mok = list()
for i in range(19):
    O_mok.append(list(map(int,input().split())))

flag = True
count_b = 0
count_w = 0

for start_x in range(15):
    for start_y in range(15):
        while True:
            #######################################
            for x in range(5):          # 가로 확인
                for y in range(5):
                    if O_mok[start_x + x][start_y + y] == 1:
                        count_b += 1
                    elif O_mok[start_x + x][start_y + y] == 2:
                        count_w += 1
                    else:
                        count_b = 0
                        count_w = 0
                        break
                if count_b ==5:
                    print('1')
                    print('{} {}'.format(start_x + x +1, start_y +1))
                    flag = False
                    break 
                elif count_w ==5:
                    print('2')
                    print('{} {}'.format(start_x + x +1, start_y +1))
                    flag = False
                    break
            if flag == False:
                break
                    
            #################################    
            for y in range(5):      # 세로확인
                for x in range(5):
                    if O_mok[x + start_x][y + start_y] == 1:
                        count_b += 1
                    elif O_mok[x + start_x][y + start_y] == 2:
                        count_w += 1
                    else:
                        count_b = 0
                        count_w = 0
                        break
                    
                if count_b ==5:
                    print('1')
                    print('{} {}'.format(start_x +1, start_y + y + 1))
                    flag = False
                    break 
                elif count_w ==5:
                    print('2')
                    print('{} {}'.format(start_x +1, start_y + y + 1))
                    flag = False
                    break
            if flag == False:
                break

            ####################################
            for x in range(5):      # 대각선 확인
                if O_mok[x + start_x][x + start_y] == 1:
                        count_b += 1
                elif O_mok[x + start_x][x + start_y] == 2:
                        count_w += 1
                else:
                    count_b = 0
                    count_w = 0
                    break
            if count_b ==5:
                print('1')
                print('{} {}'.format(start_x +1, start_y +1))
                flag = False
                break 
            elif count_w ==5:
                print('2')
                print('{} {}'.format(start_x +1, start_y +1))
                flag = False
                break

            ######################################
            for x in range(5):      # 역대각선 확인
                if O_mok[x + start_x][4-x + start_y] == 1:
                        count_b += 1
                elif O_mok[x + start_x][4-x + start_y] == 2:
                        count_w += 1
                else:
                    count_b = 0
                    count_w = 0
                    break
            if count_b ==5:
                print('1')
                print('{} {}'.format(start_x +1 + 4, start_y +1))
                flag = False
                break 
            elif count_w ==5:
                print('2')
                print('{} {}'.format(start_x +1 + 4, start_y +1))
                flag = False
                break
            
            ################################ 끝
            if count_b != 5 and count_w !=5:
                break
        if flag == False:
                    break
    if flag == False:
                    break
if count_b != 5 and count_w !=5:
    print('0')
#############################################################
def omok(li): [0,1,1,1,1,2,0]
    count_1 = 0
    count_2 = 0
    pos = 0
    for i in li:
        pos += 1
        if i == 1:
            count_1 +=1
            if count_2 == 5: # 
                # print('2')
                # print(pos) # 상당히 비효율 적인데?
                return 2
                break
        elif i == 2:
            count_2 += 1
            if count_1 == 5:
                return 1
                break
        else: 
            if count_1 == 5:
                return 1
                break
            elif count_2 == 5:
                return 2
                break
            else:
                count_1 = 0
                count_2 = 0
    return 0



O_mok = list()
O_mok.append([0]*20)
for i in range(19):
    O_mok.append(list(map(int,input().split()))+[0])
O_mok.append([0]*20)

for i in O_mok:
    if omok(i) :
        print(omok(i))
        break

col_li = list()
for y in range(19):
    for x in range(20):
        col_li.append(O_mok[x][y])
    if omok(col_li):
        print(omok(col_li))
        break
    else:
        col_li.clear

axis_li = list()
for r in range(0, 19):
    for x in range(0, 20-r):
        axis_li.append(O_mok[x+1][r+x])   
    if omok(axis_li):
        print(omok(axis_li))
        break
    else:
        axis_li.clear

for r in range(1, 19):
    for x in range(0, 20-r):
        axis_li.append(O_mok[r+x+1][x])
    if omok(axis_li):
        print(omok(axis_li))
        break
    else:
        axis_li.clear

reverse_axis_li =list()
for r in range(1,19):
    for x in range(r+1):
        reverse_axis_li.append(O_mok[r-x][x])   
    if omok(reverse_axis_li):
        print(omok(reverse_axis_li))
        break
    else:
        reverse_axis_li.clear

for r in range(0,19):
    for x in range(0,20-r):
        reverse_axis_li.append(O_mok[19-x][r+x])
    if omok(reverse_axis_li):
        print(omok(reverse_axis_li))
        print(r)
        break
    else:
        reverse_axis_li.clear
