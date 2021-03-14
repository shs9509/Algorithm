#https://www.acmicpc.net/problem/1012

def cons(li, r, c, char):  # li = 배치, scale = 배치 크기, char = 찾고자하는 값
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]
    count = 0   # 구역 숫자
    visited = [['o' for j in range(r)] for k in range(c)] # 체크용리스트
    for x in range(c):
        for y in range(r):
            if (li[x][y] in char) and (visited[x][y] != 'V'): # 찾는 값이며 방문하지 않았다!
                start_x = x
                start_y = y # x,y 그대로쓰면 밑에서 위의 for문의 xy가 바뀜
                count += 1  # 구역 추가 
                S = list()
                S.append([start_x,start_y])
                while len(S) != 0:
                    start_x, start_y = S.pop()
                    visited[start_x][start_y] = 'V' # 방문 체크해주기
                    for i in range(4):
                        X = start_x + dr[i]
                        Y = start_y + dc[i]
                        if 0 <= X < c and 0 <= Y < r:
                            if li[X][Y] in char and visited[X][Y] != 'V':
                                S.append([X,Y])
    return count

tc = int(input())
for tc_num in range(tc):
    row, col, num = list(map(int ,input().split()))
    bat = [[0 for row in range(row)] for col in range(col)]	# 밭은 0으로 이루어져있다.
    for i in range(num):
        a,b = list(map(int ,input().split()))	# 배추 좌표
        bat[b][a] = 1		# 배추가 심어진 밭의 좌표를 '1' 로 만들어준다.
    person =cons(bat,row,col,[1])
    print(person)
