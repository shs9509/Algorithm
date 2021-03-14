#https://www.acmicpc.net/problem/2468
def cons(li, size,height):  # li = 빌딩높이배치, scale = 배치 크기, height = 해당높이
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]
    count = 0   # 구역 숫자
    visited = [['o' for j in range(size)] for k in range(size)] # 체크용리스트
    for x in range(size):
        for y in range(size):
            if (li[x][y] > height) and (visited[x][y] != 'V'):   # 잠기지 않았고! 방문하지 않았다!
                start_x = x
                start_y = y # x,y 그대로쓰면 밑에서 위의 for문의 xy가 바뀜
                count += 1  # 구역 추가 
                S = list()
                S.append((start_x,start_y))
                while len(S) != 0:
                    start_x, start_y = S.pop()
                    for i in range(4):
                        X = start_x + dr[i]
                        Y = start_y + dc[i]
                        if 0 <= X < size and 0 <= Y < size:
                            if li[X][Y] > height and visited[X][Y] != 'V':
                                visited[X][Y] = 'V' # 방문 체크해주기
                                S.append((X,Y))
    return count


scale = int(input()) #배치 크기
building = list()   #빌딩 배치
section_li = list() # 각 층에 대한 값
max_val = 0
for i in range(scale):
    building.append(list(map(int, input().split())))

for x in building:  # 1층부터 가장 높은층까지 비교하기 위해 높은층의 값이 필요하다.
    if max_val <= max(x):
        max_val = max(x)

for h in range(max_val):  # 층수에 따른 빌딩 분리값을 append
    section_li.append(cons(building, scale,h))  

print(max(section_li))  # 빌딩 분리가 가장 컷던 수를 프린트한다.