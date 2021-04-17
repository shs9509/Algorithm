#https://www.acmicpc.net/problem/7562

def in_range(a,b):
    if 0<= a < scale and 0<= b < scale:
        return True
    else:
        False


def dfs(x,y):
    S = list()
    S.append((x,y))
    while S:
        X, Y = S.pop(0)
        count = visited[X][Y]
        for i in range(8):
            nx = X+dr[i]
            ny = Y+dc[i]
            if in_range(nx,ny) and visited[nx][ny] == 0:
                if nx == end_x and ny == end_y:
                    print(count)
                    return
                else:
                    visited[nx][ny] = count + 1
                    S.append((nx, ny))
    print(0)
    return



dr = [1,2,1,2,-1,-2,-1,-2]
dc = [2,1,-2,-1,2,1,-2,-1]

tc= int(input())

for tc_num in range(tc):
    scale = int(input())
    visited = [[0 for _ in range(scale)] for _ in range(scale)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited[start_x][start_y] = 1

    dfs(start_x, start_y)

