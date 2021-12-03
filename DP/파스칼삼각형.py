#https://www.acmicpc.net/submit/15489

R, C, W = map(int, input().split())
li = [[1], [1, 1]]
for i in range(2, R+W-1):
    t = [1]
    for j in range(1, i):
        t.append(li[i-1][j-1]+li[i-1][j])
    t.append(1)
    li.append(t)
res, w = 0, 1
for i in range(R-1, R+W-1):
    for j in range(w):
        res += li[i][C-1+j]
    w += 1
print(res)