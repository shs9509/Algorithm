#https://www.acmicpc.net/problem/10711

'''
주변의 . 개수가 해당 숫자보다 크거나 같으면 없어짐

'''
def in_range(a,b):
    if 0<= a < scale_x and 0<= b < scale_y:
        return True
    else:
        False

dr = [1,1,1,0,0,-1,-1,-1]
dc = [1,0,-1,1,-1,1,0,-1]

scale_x, scale_y = map(int, input().split())
li = list()
for s_x in range(scale_x):
    li.append(list(input()))

ans = 0
end = True
Q = [(1,1)]
while end:
    ans +=1
    end = False
    S = list()
    for x in range(1,scale_x-1):
        for y in range(1,scale_y-1):
            count = 0
            if li[x][y] == '.' or li[x][y] == '9':
                continue
            else:
                for i in range(8):
                    if in_range(x+dr[i],y+dc[i]) and li[x+dr[i]][y+dc[i]]=='.':
                            count +=1
                    if int(li[x][y]) <= count:
                        S.append((x,y))
                        break
    for k in S:
        a, b = k
        li[a][b] ='.'
        end = True
    print(li)
print(ans-1)

#########################################################

