#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo

# 벽돌이 떨어짐 / 
# 

from copy import deepcopy


def clean(map1, h, w):
    map2 = deepcopy(map1)
    for y in range(w):
        for x in range(h):
            if map2[x][y] == 0:
                for j in range(x, 0, -1):
                    map2[j][y] = map2[j - 1][y]
                map2[0][y] = 0
    return map2


def destroy(map1, h, w, x, y):
    counter = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    map2 = deepcopy(map1)
    s1 = [[x, y]]
    while s1:
        nx, ny = s1.pop()
        number = map2[nx][ny]
        if map2[nx][ny] == 0:
            continue
        map2[nx][ny] = 0
        counter += 1
        if number > 1:
            for i in range(1, number):
                for d in range(4):
                    nx2 = nx + i * dx[d]
                    ny2 = ny + i * dy[d]
                    if -1 < nx2 < h and -1 < ny2 < w and map2[nx2][ny2] != 0:
                        s1.append([nx2, ny2])
    return map2, counter


def solution(map1, n, h, w):
    global blocks
    answer = h * w #처음 남은벽돌값
    # 공 횟수 깨뜨린 블럭 맵
    stack = [[0, 0, map1]]
    while stack:
        count, sub, nmap = stack.pop()
        if sub==blocks: # 블럭을 다꺠뜨린경우 남은벽돌은 없음
            return 0
        if count == n: #볼을 다쓴경우
            if answer > blocks - sub:
                answer = blocks - sub
        else:
            # y축 전부 돌면서
            for y1 in range(w):
                flag = 0
                x1 = 0
                while 1:
                    if x1 == h: #끝에 도달한경우
                        flag = 1
                        break
                    elif nmap[x1][y1] == 0: # 0이면 아래로 넘어감
                        x1 += 1
                    else:
                        break #해당 [x1][y1]
                if flag == 1:
                    continue
                else:
                    nmap2, nsub = destroy(nmap, h, w, x1, y1)
                    nmap2=clean(nmap2,h,w)
                    stack.append([count + 1, sub + nsub, nmap2])
    return answer

t=int(input())
for test in range(1,t+1):
    n, w, h = map(int, input().split()) # 볼 개수, 너비,높이
    map1 = []
    blocks = 0
    for _ in range(h):
        s = list(map(int, input().split()))
        for i in s:
            if i != 0:
                blocks += 1
        map1.append(s)
    answer=solution(map1,n,h,w)
    print('#{} {}'.format(test, answer))