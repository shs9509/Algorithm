#0624 경로찾기 : https://www.acmicpc.net/problem/11403

def graph(S):
    while S:
        print(S)
        x,y = S.pop()
        for i in range(n):
            if li[y][i] == 0:
                li[y][i] = 1
                S.append((y,i))
        
            if li[x][i] == 0:
                li[x][i] = 1
                S.append((x,i))


        

n = int(input())
li = list()
s = list()
for i in range(n):
    li.append(list(map(int,input().split())))

for x in range(n):
    for y in range(n):
        if li[x][y]==1:
            s.append((x,y))

graph(s)
print(li)