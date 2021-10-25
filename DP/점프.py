n = int(input())
li = list()
for i in range(n):
    li.append(list(map(int,input().split())))

V = [[0 for _ in range(n)] for _ in range(n)]

def dp(lis):
    if lis==[]:
        return
    new_li = list()
    for L in lis:
        x,y = L
        X_under = x+li[x][y]
        Y_right = y+li[x][y]
        if 0<=X_under<n:
            if (X_under==n-1 and y==n-1):
                V[X_under][y]+=1
            else:
                V[X_under][y]+=1
                new_li.append((X_under,y))
        if 0<=Y_right<n:
            if (Y_right==n-1 and x==n-1):
                V[x][Y_right]+=1
            else:
                V[x][Y_right]+=1
                new_li.append((x,Y_right))
    # print(new_li)
    dp(new_li)


dp([(0,0)])
print(V[n-1][n-1])

##################################################################


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)] 
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1: 
            print(dp[i][j])
            break
        cur_cnt = field[i][j]
        if j + cur_cnt < N:
            dp[i][j + cur_cnt] += dp[i][j]
        if i + cur_cnt < N:
            dp[i + cur_cnt][j] += dp[i][j]