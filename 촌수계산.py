#https://www.acmicpc.net/problem/2644
'''
이거 걍 bfs 그래프문제 아닌가?
'''
def bfs(start,end): # 인자는 시작노드와 끝노드
    visit = [0 for _ in range(num+1)] # 방문과 거리표현을 위한 리스트
    S=list()    # 스택
    S.append(start) # 시작노드를 스택에 넣고
    visit[start] =1 # 거리는 1로 표시하면서 방문표시
    count = 0   # 거리
    while S:
        start = S.pop(0)
        count = visit[start] # 시작노드의 거리값을 받는다.
        count += 1 # 다음노드의 거리는 count +1
        for j in save[start]:   # 시작노드가 갖고있는 일촌들을 꺼낸다.
            if j == end:    # 꺼낸게 끝노드면 마무리
                visit[end] = count-1
                return visit[end]
            if visit[j]== 0:    # 꺼낸게 방문안한 노드이면
                visit[j] = count # 노드에 거리 새겨 주고
                S.append(j) # 스택에 넣는다.
    return -1   # 못찾았다는 것은 관계없는 사람이란것이다. -1 출력



num = int(input()) # 명수
a, b = map(int, input().split()) # 시작노드, 끝노드
E = int(input())    # 간선수
save = [[] for _ in range(num+1)] # 촌수저장 리스트
for i in range(E): # 간선수만큼 for문 돌려서 일촌상황을 저장한다.
    c,d = map(int,input().split())
    save[c].append(d)
    save[d].append(c) # 촌수는 양방향 관계!
print(bfs(a,b))




