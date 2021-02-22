#https://www.acmicpc.net/problem/10163

a = int(input())
b =[list(map(int, input().split())) for i in range(a)]
c =[[0]*101 for _ in range(101)]    # 101x101 의 0으로 꽉찬 색종이
for i in range(len(b)):
    for x in range(b[i][0], b[i][0] + b[i][2]):
        for y in range(b[i][1], b[i][1] + b[i][3]): #색종이 넓이만큼 자기의 인덱스값으로 채운다.
            c[y][x] = i+1                           #같은 자리이면 덮어씌어진다.

answer = [0]*len(b) 
for i in range(len(b)):
    for x in range(101):
        for y in range(101):
            if c[x][y] == i+1:  # 인덱스값이 몇개있는지 각각 확인
                answer[i] += 1

for i in answer:
    print(i)

'''
 출력되는데 겁나오래걸림
 101칸인줄 모르고 100칸했더니 오류떠서 좀 걸림
'''