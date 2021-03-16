from collections import deque

def bfs():
    q = deque()
    q.append(subin)
    while q:
        x = q.popleft()
        if x == brother: # 동생자리에 도달했을 경우
            print(li[x])
            break
        for pos in (x-1,x+1,x*2): # 자리를 움직이자 pos = x+1, x-1, x*2   ex. 6,4,10
            if 0 <= pos <= MAX and not li[pos]: # 움직인자리가 범위를 벗어나지않고 , 0인 경우
                li[pos] = li[x]+1   # 5엿으니 6,4,10 자리에 +1(횟수) 체크됨 # li[x]는 횟수를 이어받기위함
                q.append(pos)

MAX = 10 ** 5
li = [0]*(MAX + 1)
subin, brother = list(map(int, input().split())) # 5, 17
bfs()
