#0711 명제증명 : https://www.acmicpc.net/problem/2224
import copy
def graph(start,tmp): #A,b
    tmp.append(start)
    for position in li:
        if position[0] == start:
            if position[1] in tmp:
                continue
            else:
                graph(position[1],tmp)
                break
    else:
        result.append(tmp)
        return

def per(start,t,spe):
    global answer
    if len(t)==2:
        if t not in answer:
            c = copy.copy(t)
            answer.append(c)
        return
    for n in range(start,len(spe)):
        t.append(spe[n])
        per(n+1,t,spe)
        t.pop()


tc = int(input())
li = list()
for i in range(tc):
    tmp = list(input().split())
    li.append([tmp[0], tmp[-1]])

S =[]

for j in li:
    if j[0] not in S:
        S.append(j[0])
    if j[1] not in S:
        S.append(j[1])

answer = []
result = []

for k in S:
    # flag = False
    # for j in result:
    #     if k in j:
    #         flag = True
    #         break
    # if flag:
    #     continue
    # else:
    graph(k,[])
print(result)
#[[A,b,C],[b,C], [C]]
for m in result:
    per(0,[],m)

print(answer)
answer = sorted(answer)
print(len(answer))
for b in answer:
    an_s , an_e = b
    print(an_s+" => "+an_e)



#############################################################
# import sys
 
# input = sys.stdin.readline
# INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
 
# # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# graph = [[INF] * (52) for _ in range(52)]
 
# for _ in range(int(input())):
#     a, b, c = input().split()
 
#     a_ord = ord(a)
#     c_ord = ord(c)
 
#     # 소문자
#     if a_ord >= ord('a'):
#         a_ord = a_ord - (ord('a') - ord('Z') - 1)
#     # 소문자
#     if c_ord >= ord('a'):
#         c_ord = c_ord - (ord('a') - ord('Z') - 1)
 
#     a_ord = a_ord - ord('A')
#     c_ord = c_ord - ord('A')
 
#     graph[a_ord][c_ord] = 1
 
# # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# for a in range(52):
#     for b in range(52):
#         if a == b:
#             graph[a][b] = 0
 
# # 점화식에 따라 플로이드 워셜 알고리즘을 수행
# for k in range(52):
#     for a in range(52):
#         for b in range(52):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
 
# arr = []
# # 수행된 결과를 출력
# for a in range(52):
#     for b in range(52):
#         # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#         if graph[a][b] == 0 or graph[a][b] == 1e9:
#             pass
#         # 도달할 수 있는 경우 거리를 출력
#         else:
#             arr.append(a)
#             arr.append(b)
#             # print(graph[a][b], end=" ")
 
# print(len(arr) // 2)
# for i in range(0, len(arr), 2):
#     # print(arr[i], arr[i+1])
#     a = arr[i]
#     c = arr[i + 1]
 
#     # 소문자
#     if a > 25:
#         a = a + (ord('a') - ord('Z') - 1)
#     # 소문자
#     if c > 25:
#         c = c + (ord('a') - ord('Z') - 1)
 
#     a = a + ord('A')
#     c = c + ord('A')
 
#     print("%c => %c" % (chr(a), chr(c)))
####################################################
_INF = 1e9
def solution():
    N = int(input())
    Floyd = [[_INF for _ in range(52)] for _ in range(52)]

    for _ in range(N):
        answer = (input().split(' '))
        #[A,=>,C]
        dx, dy = 0, 0
        if 'A' <= answer[0] <= 'Z': dx = ord(answer[0]) - 65
        else: dx = ord(answer[0]) - 71
        if 'A' <= answer[2] <= 'Z': dy = ord(answer[2]) - 65
        else: dy = ord(answer[2]) - 71

        Floyd[dx][dy] = 1

    for k in range(52):
        for i in range(52):
            for j in range(52):
                Floyd[i][j] = min(Floyd[i][j], Floyd[i][k] + Floyd[k][j])

    cnt = 0
    for i in range(52):
        for j in range(52):
            if i == j: continue
            if Floyd[i][j] != _INF:
                cnt += 1
    print(cnt)
    for i in range(52):
        for j in range(52):
            ret = ''
            if i == j: continue
            if Floyd[i][j] == _INF:
                continue
            if 0 <= i < 26: ret += chr(i + 65)
            else: ret += chr(i + 71)

            ret += ' => '

            if 0 <= j < 26: ret += chr(j + 65)
            else: ret += chr(j + 71)

            print(ret)

solution()