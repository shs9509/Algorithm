import copy

check =[]
def distance(x,y,li,count):
    nonlocal check
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    if count == 3:
        return 1
    for i in range(4):
        X = dx[i]+x
        Y = dy[i]+y
        if 0<=X<5 and 0<=Y<5 and li[X][Y]!="X":
            if li[X][Y]=="P":
                check.append(0)
                return 0
            else:
                tmp = copy.deepcopy(li)
                tmp[X][Y] = "C"
                distance(X,Y,tmp,count+1)
    else:
        check.append(1)
        return 1
def distance_check(li):
    nonlocal check
    for x in range(5):
        for y in range(5):
            if li[x][y]=="P":
                check =[]
                li[x][y] = "C"
                if distance(x,y,li,0) and 0 not in check:
                    li[x][y] ="P"
                else:
                    return 0
    return 1
            
def solution(places):
    answer = []
    for place in places:
        for i in range(5):
            place[i] = list(place[i])
        answer.append(distance_check(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))


/////////////
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer