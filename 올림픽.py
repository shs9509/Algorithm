#https://www.acmicpc.net/problem/8979
a,b = list(map(int, input().split()))
c = list()
for i in range(a):
    c.append(list(map(int, input().split())))

for k in range(len(c)):
    c[k].append(int(k)+1)

for n in range(len(c)-1):
    for j in range(len(c)-n-1):
        if c[j][1] < c[j+1][1]:
            c[j][4] ,c[j+1][4] = c[j+1][4], c[j][4]  
            c[j], c[j+1] = c[j+1], c[j]

for n in range(len(c)-1):
    for p in range(len(c)-n-1):
        if c[p][1] == c[p+1][1] and c[p][2] < c[p+1][2]:
            c[p][4] ,c[p+1][4] = c[p+1][4], c[p][4]
            c[p], c[p+1] = c[p+1], c[p]

for n in range(len(c)-1):
    for y in range(len(c)-n-1):        
        if c[y][1] == c[y+1][1] and c[y][2] == c[y+1][2] and c[y][3] < c[y+1][3]:
            c[y][4] ,c[y+1][4] = c[y+1][4], c[y][4]
            c[y], c[y+1] = c[y+1], c[y]
    
for z in range(len(c)-1):
    if c[z][1] == c[z+1][1] and c[z][2] == c[z+1][2] and c[z][3] == c[z+1][3]:
        c[z+1][4] = c[z][4]


for f in c:
    if f[0] == b:
        print(f[4])

## 뭉치면 오류난다.
## for문이 같은 레벨에 있다면 안심하고 같은 변수를 써도된다.
## 금메달 은메달 동메달 세우고 따라란한다.
## 비효율 적인거같은데 이것이 최선일까?
## 배웠던 버블정렬을 쓴거 같다.
## sorted 와 람다를 쓴다면 쉬워진다. 람다 공부하자.